Title: Transparent WinForms Label
Date: 2009-11-28 12:40
Author: Eric
Category: Programming
Tags: .NET, User Interface, Windows
Slug: transparent-winforms-label
Status: published

Easy control transparency isn't exactly a hallmark of Windows Forms. If
you have a form with a background image or a gradient, the stock
controls paint with a solid background to give a criminally egregious
aesthetic.

<!--more-->If you search the web for a solution, you might come up with
a couple of proposed solutions:

-   [WinForms: How to create a control transparent to other
    controls](http://support.microsoft.com/kb/943454) - The official
    word from Microsoft, the solution is presented in several pages of
    poorly formatted VB code that makes you immediately want to look for
    something simpler, such as...
-   [C\# Transparent Label](http://www.doogal.co.uk/transparent.php)
    (also
    [referenced](http://www.west-wind.com/WebLog/posts/247977.aspx) from
    Rick Strahl's blog) - This solution is much simpler; it's just a
    Control subclass that doesn't paint a background and draws the label
    text in OnPaint.

After working with the second solution for a while, I discovered that it
doesn't handle updating the text very well. Just changing the Text
property itself doesn't do it, and if you invalidate the control, you
get the new text painted over the old text. If you're the kind of person
who fusses about minutiae like *legibility* and such, this isn't ideal.

So here's a solution that has worked reasonably well for me, and that
scores high marks in the simplicity category:

```csharp
/// 
/// A label that is transparent.
/// 
public class TransparentLabel : Label
{
  /// 
  /// Paints the background with the parent's background image.
  /// 
  ///
e
  protected override void OnPaintBackground(PaintEventArgs e)
  {
    Rectangle rect = new Rectangle(Location, Size);
    e.Graphics.DrawImage(Parent.BackgroundImage, 0, 0, rect, GraphicsUnit.Pixel);
  }
}
```

It basically scoops up the correct part of the parent's background image
and uses it as the background for the control. Yes, it still isn't
transparency, just a much better job of "camouflage" than the default
behavior. If you're painting the parent's background, with a gradient
brush for example, you can paint that into a bitmap instead and set the
parent's BackgroundImage to the bitmap for this solution to still work.
