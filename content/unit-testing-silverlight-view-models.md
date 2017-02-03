Title: Unit Testing Silverlight View Models
Date: 2009-06-08 09:16
Author: Eric
Category: How-To
Tags: Silverlight
Slug: unit-testing-silverlight-view-models
Status: published

Being relatively new to Silverlight development, I've not had the good
sense to accept conventional wisdom that the Visual Studio unit test
framework can't be used to test Silverlight code. For testing view
models at least, I've been successfully using Mstest and Rhino Mocks for
a few months now.

<!--more-->

One of the goals of the *model-view-view model* pattern is to avoid code
in the XAML code-behind files. Instead, the view model exposes what the
UI needs and the UI consumes it through declarative data binding. [Shawn
Wildermuth's MSDN Magazine
article](http://msdn.microsoft.com/en-us/magazine/dd458800.aspx) does a
good job of explaining the basics of the pattern. The view model ends up
having the logic that you'd really like to test.

The project structure looks like this:

-   **SilverlightApp** - This project is the *view*, created with the
    Visual Studio Silverlight Application project template. There's lots
    of XAML in here.
-   **SilverlightApp.Model** - This project contains both the *model*
    and the *view model*. It is a Silverlight Class Library project, and
    the view project has a project reference to this. There's no XAML
    in here.
-   **SilverlightApp.Model.Test** - This project has the unit tests, and
    is a normal C\# Unit Test project. It has a project reference to the
    model/view model project.

If you write up a simple unit test, it will compile, run, and pass.

![Woohoo -- passing test]({filename}/images/test-passed.jpg)

**Problem \#1**

Suppose your view model uses something from System.Core (such as the
Action delegate). Now when you try to run your unit test, you get an
error:

> Test method SilverlightApp.Model.Test.UnitTest.TestMethod1 threw
> exception:  System.IO.FileNotFoundException: Could not load file or
> assembly 'System.Core, Version=2.0.5.0, Culture=neutral,
> PublicKeyToken=7cec85d7bea7798e' or one of its dependencies. The
> system cannot find the file specified.

The problem is that the test project is referencing the .NET 3.5
System.Core assembly. You can fix that by referencing the Silverlight
assembly instead. Remove the existing System and System.Core references,
and add the ones in the Silverlight SDK (for example, C:\\Program Files
(x86)\\Microsoft SDKs\\Silverlight\\v2.0\\Reference Assemblies\\). Now
the test will pass again.

**Problem \#2**

Now suppose that you want your view model to do something like use the
IsolatedStorageSettings class. When you run your test, it will be broken
again:

> Test method SilverlightApp.Model.Test.UnitTest.TestMethod1 threw
> exception:  System.IO.FileNotFoundException: Could not load file or
> assembly 'System.Windows, Version=2.0.5.0, Culture=neutral,
> PublicKeyToken=7cec85d7bea7798e' or one of its dependencies. The
> system cannot find the file specified.

Well, that just looks like problem \#1 again, so we'll add the
Silverlight System.Windows assembly as a reference. Hmm... still doesn't
work:

> Test method SilverlightApp.Model.Test.UnitTest.TestMethod1 threw
> exception:  System.MissingMethodException: Method not found:
> 'System.IO.IsolatedStorage.IsolatedStorageFile
> System.IO.IsolatedStorage.IsolatedStorageFile.GetUserStoreForSite()'.

According to the
[documentation](http://msdn.microsoft.com/en-us/library/system.io.isolatedstorage.isolatedstoragefile(VS.95).aspx),
IsolatedStorageFile is in mscorlib.dll. Can I just add a reference to
that? No; when you try you get an error:

> A reference to 'C:\\Program Files (x86)\\Microsoft
> SDKs\\Silverlight\\v2.0\\Reference Assemblies\\mscorlib.dll' could not
> be added. This component is automatically referenced by the project
> system and cannot be referenced directly.

It's time to step back and think a little. Do we really want to have
Silverlight isolated storage as part of our unit tests anyway? Probably
not. Just like when you're unit testing code that would access a
database, you'd really rather mock the database so you can efficiently
test just the unit in question. The same applies here, so you can create
an interface to hide the concrete implementation. From there, it's a
matter of choosing the right implementation at the right time.

The view model can accept an ISettings in its constructor (or it can use
a service locator or dependency injection). When creating a test
instance, pass in a mock implementation. In the real application, you
can use the isolated storage implementation.

**So Far So Good**

By using these two techniques (referencing Silverlight assemblies in the
test project and adding a level of abstraction where needed), I've been
able to effectively test my view models with the normal desktop tools.
The tests all run as part of the continuous integration builds, just as
you'd hope.

Maybe at some point I'll run into something that just doesn't work, but
so far it's working out just fine.
