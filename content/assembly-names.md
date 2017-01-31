Title: Assembly Names
Date: 2007-05-07 21:21
Author: Eric
Tags: .NET
Slug: assembly-names
Status: published

I always have a hard time keeping straight all the possible ways of
getting an assembly's name and what form the various methods return.
Here's a little program and its output for a reference.

<!--more-->

```csharp
class Program 
{ 
    static void Main(string[] args) 
    { 
        Assembly assembly = Assembly.GetExecutingAssembly(); 
        Console.WriteLine("Assembly.ToString()           : {0}", assembly.ToString()); 
        Console.WriteLine("Assembly.FullName             : {0}", assembly.FullName); 
        Console.WriteLine("Assembly.GetName().ToString() : {0}", assembly.GetName().ToString()); 
        AssemblyName assemblyName = assembly.GetName(); 
        Console.WriteLine("AssemblyName.FullName         : {0}", assemblyName.FullName); 
        Console.WriteLine("AssemblyName.Name             : {0}", assemblyName.Name); 
    } 
}
```

**Output:**

```
Assembly.ToString()           : MyAssembly, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null 
Assembly.FullName             : MyAssembly, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null 
Assembly.GetName().ToString() : MyAssembly, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null 
AssemblyName.FullName         : MyAssembly, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null 
AssemblyName.Name             : MyAssembly
```

Basically, most of the methods return the complete assembly name (and
the PublicKeyToken would be non-null if the assembly were strongly
named). To get the short name of the assembly, you need to get the
`AssemblyName` object's `Name` property.
