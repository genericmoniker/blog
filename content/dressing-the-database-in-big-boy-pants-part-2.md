Title: Dressing the Database in Big-Boy Pants, Part 2
Date: 2013-04-13 14:45
Author: Eric
Category: How-To
Tags: database
Slug: dressing-the-database-in-big-boy-pants-part-2
Status: published

[Last time]({filename}/dressing-the-database-in-big-boy-pants-part-1.md)
I wrote about using dbdeploy to easily create local databases and to
automatically apply changes to the development, staging and production
databases. The other change I made recently was to add **stored
procedure unit tests**.

<!--more-->

I looked briefly at frameworks specifically for testing databases, but
didn't see a ton of value beyond just invoking the database from JUnit
via JDBC, so that's what I did. Like the use of dbdeploy, stuff gets
started from Ant, with a `test` target.

```xml
<target name="test" depends="create-test-database"
    description="Run tests against database procedures">
    <path id="test.lib.path">
      <fileset dir="lib">
        <include name="**/*.jar"/>
      </fileset>
      <fileset dir="test/lib">
        <include name="**/*.jar"/>
      </fileset>
    </path>
    <!-- Compile tests -->
    <mkdir dir="${target.dir}/classes"/>
    <javac srcdir="test/src" destdir="${target.dir}/classes" includeantruntime="false">
        <classpath>
            <path refid="test.lib.path"/>
        </classpath>
    </javac>
    <!-- Run them -->
    <junit printsummary="on" haltonfailure="on">
        <sysproperty key="dbhost" value="${db.host}"/>
        <sysproperty key="dbuser" value="${db.user}"/>
        <sysproperty key="dbpass" value="${db.password}"/>
        <sysproperty key="dbname" value="${test.db.name}"/>
        <classpath>
            <path refid="test.lib.path"/>
            <pathelement location="${target.dir}/classes"/>
        </classpath>
        <batchtest>
           <fileset dir="test/src">
                <include name="**/*Test*" />
           </fileset>
        </batchtest>
    </junit>
</target>
```

Since it is trivial to create a fresh database, I create a separate one
just for testing in the dependent `create-test-database` target. This
lets passing tests be a precondition to updating the real database. In
other words, on the build server, the `test` target has to succeed
before the `update-database` target will be run that will apply the
current set of database deltas to the real database.

The `sysproperty` Ant task is handy here because it lets you pass
information to the JUnit tests. This means you can set all the database
connection information once in the Ant script, but have access to it in
the JUnit tests, keeping things
[DRY](http://en.wikipedia.org/wiki/Don't_repeat_yourself).

In JUnit, the properties set with the `sysproperty` task are available
via `System.getProperty`, as you can see from this setup function:

```java
@BeforeClass
public static void classSetUp() throws Exception {
    // Get database connection info from system properties set by Ant.
    String host = System.getProperty("dbhost");
    String database = System.getProperty("dbname");
    String user = System.getProperty("dbuser");
    String password = System.getProperty("dbpass");

    Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
    String connectionUrl = String.format("jdbc:sqlserver://%s;database=%s;user=%s;password=%s",
                host, database, user, password);
    conn = DriverManager.getConnection(connectionUrl);

    String sql = "DECLARE @RC int; EXEC @RC = [dbo].[UpdateCamera2] ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?; SELECT 'Return Value' = @RC";
    spStatement = conn.prepareStatement(sql);
}
```

This gets everything set up to call the stored procedure (UpdateCamera2
in this case) as well as save the return value, with cleanup in a tear
down method:

```java
@AfterClass
public static void classTearDown() throws Exception {
    spStatement.close();
    conn.close();
}
```

There's a helper method to call the stored procedure too. This stored
procedure is pretty unwieldy because it was specifically introduced to
reduce trips to the database for a performance critical part of the
system, and it needs a lot of parameters to do its big pile o' work.

```java
/**
 * Call the stored procedure with the unwieldy list of parameters. Sorry.
 * @return A bit field whose value depends on whether the site and camera were new or already existing.
 * @throws SQLException
 */
private int execUpdateCamera2(String cameraMac,
                              String cameraName,
                              int cameraProductId,
                              String cameraFirmware,
                              String cameraInternalIPAddress,
                              String cameraIPAddress,
                              String cameraIPCountry,
                              boolean cameraAlertsEnabled,
                              String cameraJidResource,
                              String siteId,
                              String siteName,
                              int siteAlertFilter,
                              int siteAlertFrequency) throws SQLException {
    spStatement.setString(1, "testuser@dvsopstest.com");
    spStatement.setString(2, "unit test");
    spStatement.setString(3, cameraMac);
    spStatement.setString(4, cameraName);
    spStatement.setInt(5, cameraProductId);
    spStatement.setString(6, cameraFirmware);
    spStatement.setString(7, cameraInternalIPAddress);
    spStatement.setString(8, cameraIPAddress);
    spStatement.setString(9, cameraIPCountry);
    spStatement.setBoolean(10, cameraAlertsEnabled);
    spStatement.setString(11, cameraJidResource);
    spStatement.setString(12, siteId);
    spStatement.setString(13, siteName);
    spStatement.setInt(14, siteAlertFilter);
    spStatement.setInt(15, siteAlertFrequency);

    spStatement.execute();

    ResultSet results = spStatement.getResultSet();
    results.next();
    int returnValue = results.getInt(1);
    results.close();

    return returnValue;
}
```

With all that set up, an individual unit test (that references a couple
of other helper methods) looks like this:

```java
@Test
/**
 * A new site is created if the provided site info doesn't match an existing site.
 */
public void newSiteCreated() throws Exception {
    String siteId = UUID.randomUUID().toString();
    String siteName = "Test Site #1";
    int siteAlertFilter = 111;
    int siteAlertFrequency = 1111;

    int result = execUpdateCamera2("11-11-11-11-11", "Unit Test Camera", 16, "1.0", "", "", "-", true, "TestJID",
            siteId, siteName, siteAlertFilter, siteAlertFrequency);

    assertFalse(siteExisted(result));
    HashMap site = queryForSite(siteId);
    assertEquals(siteName, site.get("Name"));
    assertEquals(siteAlertFilter, site.get("AlertFilter"));
    assertEquals(siteAlertFrequency, site.get("AlertFrequency"));
}
```

I recently had to update this stored procedure, and let me tell you, I
didn't get it right the first time. Or even the third or fourth time. So
it was fantastic to have a procedure that took just a few seconds to
spin up a clean test database with my latest attempt and run though all
the tests. When I finally worked through my SQL mistakes such that the
tests passed, I was confident to check in my new delta script.
