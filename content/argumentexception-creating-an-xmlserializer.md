Title: ArgumentException Creating an XmlSerializer
Date: 2007-05-26 14:00
Author: Eric
Category: How It Works
Tags: .NET, Bafflers
Slug: argumentexception-creating-an-xmlserializer
Status: published

I ran into a kind of baffling problem. I've got some .NET code that is
also accessible to Java via JNI. There are unit tests for the .NET code
that all pass. To test the Java to .NET connection, I wrote a few JUnit
tests which worked fine when run from the IDE, but failed when run from
Ant. The failure was ultimately caused by an ArgumentException when
creating an XmlSerializer.

<!--more-->

The exception was thrown from line 5 in the code below.

```csharp
public static FileTypeHandlerCatalog Load(string fileName)
{
using (StreamReader reader = new StreamReader(fileName))
    {
        XmlSerializer serializer = new XmlSerializer(typeof(FileTypeHandlerCatalog));
        FileTypeHandlerCatalog catalog = (FileTypeHandlerCatalog)serializer.Deserialize(reader);
        catalog.Validate();
        return catalog;
    }
}
```
The exception message wasn't terribly helpful either since it was
obviously disgorging implementation details from somewhere deep in the
XmlSerializer class:

`System.ArgumentException: Item has already been added. Key in dictionary: 'path' Key being added: 'path'`

The stack trace led me to the
`System.CodeDom.Compiler.Executor.ExecWaitWithCaptureUnimpersonated`
method, which contains the following bit of code:

```csharp
StringDictionary sd = new StringDictionary();
foreach (DictionaryEntry entry in Environment.GetEnvironmentVariables())
{
    sd.Add((string) entry.Key, (string) entry.Value);
}
```

I guess it is copying the environment variables so that it can add a new
one related to security. The problem is that when running under Ant, for
some reason there were three different PATH environment variables with
an assortment of cases: PATH, Path and path. Looking at the
`StringDictionary.Add` implementation, the problem became clear. In line
7, it converts the key to lower case in order to add it to the hash
table, resulting in duplicate keys.

```csharp
public virtual void Add(string key, string value)
{
    if (key == null)
    {
        throw new ArgumentNullException("key");
    }
    this.contents.Add(key.ToLower(CultureInfo.InvariantCulture), value);
}
```

So it appears to be a bug in the Executor class -- it doesn't expect to
encounter multiple keys in the environment variable dictionary that
differ only by case.

I solved the problem by pregenerating the serialization assembly using
sgen, which is generally a good idea anyway.
