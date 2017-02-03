Title: Silverlight Localization
Date: 2009-07-08 20:00
Author: Eric
Category: How-To
Tags: Silverlight
Slug: silverlight-localization
Status: published

The official [Silverlight documentation about
localization](http://msdn.microsoft.com/en-us/library/cc838238(VS.95).aspx)
gives lots of information about working with resource files, but it is
kind of scant on how to actually get localized strings to show up in the
UI in a reasonable way. For example, an unreasonable way would be to set
the text/content properties of all the controls in a page's code-behind
file. A reasonable way is to use data binding.

I found a good example of this in Chapter 5 of *Professional Silverlight
2 for ASP.NET Developers* by Jonathan Swift, Salvador Alvarez Patuel,
Chris Barker and Dan Wahlin. As I describe it, and continue the
discussion through this post, you'll notice that the term "resource" is
overloaded in Silverlight: There are resources in the normal .NET sense,
backed by .resx files, and there are resources that are simply a
dictionary of objects instantiated in XAML within a Resources element.
Hopefully the usage will not be overly confusing.

In the localization example from the book, they created a resource file
called LocalizedStrings.resx. Then they instantiated the automatically
generated strongly typed class by including it in the Resources
associated with a user control. Finally, they could then bind the Text
property of a couple of TextBlock controls to a particular string from
the resources:

```xml
<UserControl x:Class="SilverlightLocalizationExample.Page"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:Localized="clr-namespace:LocalizationExample.Resources">

    <UserControl.Resources>
        <Localized:LocalizedStrings x:Name="LocalizedStrings" />
    </UserControl.Resources>

    <StackPanel x:Name="LayoutRoot" Background="LightBlue">

        <TextBlock Text="{Binding TextBlock1,
            Source={StaticResource LocalizedStrings}}" />

        <TextBlock Text="{Binding TextBlock2,
            Source={StaticResource LocalizedStrings}}" />

    </StackPanel>

</UserControl>
```

You'll want to be sure to use the PublicResXFileCodeGenerator custom
tool to generate the code from the .resx file, otherwise the binding
doesn't work.

So what if you want to dynamically change languages, such as with a
language drop-down?

The solution I came up with incorporates string resources into the view
model. I was hesitant to do this at first because it felt funny having
resources in the view model. Aren't the strings purely a view component?
Ultimately I decided that supplying the correct strings to the view
based on language choice is a reasonable thing for the view model to do,
and the resulting implementation and usage felt pretty good.

The base class for all view models simply has a Resources member:

```csharp
public virtual object Resources
{
  get { return null; }
}
```

Each subclass then returns the appropriate object containing the
resources:

```csharp
public class MyViewModel : ViewModel
{
  private MyViewModelResources _resources;

  MyViewModel()
  {
    _resources = new MyViewModelResorces();
  }

  public override object Resources
  {
    get { return _resources; }
  }

  // ...
}
```

The class MyViewModelResources is the class generated from
MyViewModelResources.resx. You might be saying, "Wait a minute. That
class is basically *static*. What are you doing creating an instance of
it?" Well, I don't think there's a way to bind to statics, so you need
to have an actual instance around. Of course, the view will actually end
up calling the static property (such as SubmitButtonText) when you
include one in the binding path. Also, this isn't any different from
instantiating the resource class in XAML as the first example does.

Modifying the first example to use the view model (and setting the view
model as the DataContext) makes the XAML look like this:

```xml
<UserControl x:Class="SilverlightLocalizationExample.Page"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:Localized="clr-namespace:LocalizationExample">

    <UserControl.Resources>
        <Localized:MyViewModel x:Name="ViewModel" />
    </UserControl.Resources>

    <StackPanel x:Name="LayoutRoot" Background="LightBlue" 
        DataContext="{StaticResource ViewModel}">

        <TextBlock Text="{Binding Resources.TextBlock1}" />

        <TextBlock Text="{Binding Resources.TextBlock2}" />

    </StackPanel>

</UserControl>
```

So what about the dynamic switching of languages at run time?

Since the "Resources" property is in the binding path, changing its
value will update the bindings and the UI updates with the new strings.
You just need to notify the view that the Resources property has
changed. To make this easy, I created a helper method in the ViewModel
base class, RaiseResourcesChanged, that effectively says, "Attention all
view models, please update your views' resources." The message gets
propagated to each view model instance by having a static
ResourcesChanged event in the ViewModel base class that each ViewModel
instance subscribes to at construction. When the event fires, the base
class in turn raises the INotifyPropertyChanged.PropertyChanged event
for the "Resources" property.

```csharp
public class ViewModel : INotifyPropertyChanged
{
  private static event EventHandler ResourcesChanged;

  public ViewModel()
  {
    ResourcesChanged += ViewModel_ResourcesChanged;
  }

  protected void RaiseResourcesChanged()
  {
    var handler = ResourcesChanged;
    if (handler != null)
    {
      ResourcesChanged(this, EventArgs.Empty);
    }
  }

  void ViewModel_ResourcesChanged(object sender, EventArgs e)
  {
    RaisePropertyChanged("Resources");
  }

  // ...
}
```

Any single view model can then change the CurrentUICulture, call the
helper method, and the UI updates automatically for all views:

```csharp
Thread.CurrentThread.CurrentUICulture = newCulture;
RaiseResourcesChanged();
```
