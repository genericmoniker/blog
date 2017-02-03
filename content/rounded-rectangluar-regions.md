Title: Rounded Rectangluar Regions
Date: 2009-11-19 22:27
Author: Eric
Category: How-To
Tags: .NET, Windows
Slug: rounded-rectangluar-regions
Status: published

There are lots of examples that demonstrate how to draw a rectangle with
rounded corners using GDI+ in .NET. Converting such a rectangle to a
Region so that it can be filled or be used for the geometry of a window
can have less than perfect results, though.

For example, here is one of the more concise methods for getting a
rounded Rectangle:

```csharp
public static GraphicsPath GetRoundedRectangle(Rectangle rect, int rad)
{
    int d = 2 * rad;
    System.Drawing.Drawing2D.GraphicsPath gp =
            new System.Drawing.Drawing2D.GraphicsPath();

    gp.AddArc(rect.X, rect.Y, d, d, 180, 90);
    gp.AddArc(rect.X + rect.Width - d, rect.Y, d, d, 270, 90);
    gp.AddArc(rect.X + rect.Width - d, rect.Y + rect.Height - d, d, d, 0, 90);
    gp.AddArc(rect.X, rect.Y + rect.Height - d, d, d, 90, 90);
    gp.AddLine(rect.X, rect.Y + rect.Height - d, rect.X, rect.Y + d / 2);

    return gp;
}
```

It's trivial to convert that GraphicsPath to a Region -- just call the
appropriate Region constructor. You can then fill the region:

```csharp
var path = GetRoundedRectangle(rect, 3);
e.Graphics.FillRegion(Brushes.Orange, new Region(path));
```

If your corner radius is sufficiently large, you might not notice
anything wrong with the result. With a value of 3, it is pretty obvious:

![Not-so-rounded
rectangle]({filename}/images/rect-bad.png "Not-so-rounded rectangle")

The top left corner looks perfect:

![Top-left]({filename}/images/rect-topleft.png "Top-left")

The bottom right corner is decidedly un-round:

![Bottom-right]({filename}/images/rect-bottomright1.png "Bottom-right")

I started to wonder if all those round rectangle functions were wrong,
but drawing the GraphicsPath itself shows that the code is correct:

![Graphics
Path]({filename}/images/rect-path.png "Graphics Path")

The problem is that when converting the GraphicsPath to a Region, it
uses the *inside* of the GraphicsPath, so you lose the outside pixels on
the sides, which you can see when drawing the path and then filling the
region:

![rect-detail]({filename}/images/rect-detail.png "Missing pixels in the region")

It turns out to be a whole lot easier and effective to do a little
p/invoke here:

```csharp
[DllImport("gdi32.dll")]
static extern IntPtr CreateRoundRectRgn(int x1, int y1, int x2, int y2, int cx, int cy);
// ...
var region = Region.FromHrgn(CreateRoundRectRgn(rect.X, rect.Y, rect.X + rect.Width, rect.Y + rect.Height, 3, 3));
e.Graphics.FillRegion(Brushes.Orange, region);
```

Here's the output from that code:

![Good
Region]({filename}/images/rect-good.png "Good Region")

It looks like a little larger corner radius is needed to get the same
rounding, but otherwise it is perfect.
