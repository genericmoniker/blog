Title: .NET Color Struct Equality 
Date: 2009-12-16 18:47
Author: Eric
Category: How It Works
Tags: .NET, Bafflers
Slug: net-color-struct-equality
Status: published

When is white not white? When one is `Color.White` and the other is
`Color.FromArgb(0xff, 0xff, 0xff, 0xff)`.

<!--more-->
I was trying to data bind a list of colors to a `ComboBox` and
have the `SelectedValue` property bound to a particular color. The
frustrating thing was that even though there was a color matching the
"selected" color in the list, the `ComboBox` never had a selection when
first displayed.

Eventually I discovered that my "selected" color was white (all color
components at 255) while the list's equivalent was `Color.White`.
Careful reading of the
[`Color.Equals`](http://msdn.microsoft.com/en-us/library/e03x8ct2.aspx)
documentation tells me that I was silly to think that white is white or
black is black:

> [`Black`](http://msdn.microsoft.com/en-us/library/system.drawing.color.black.aspx)
> and `FromArgb(0,0,0)` are not considered equal, since
> [`Black`](http://msdn.microsoft.com/en-us/library/system.drawing.color.black.aspx)
> is a named color and `FromArgb(0,0,0)` is not.
