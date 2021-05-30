Title: Paste Special Macro for Word
Date: 2007-12-31 13:47
Author: Eric
Category: How-To
Tags: Microsoft Office
Slug: paste-special-macro-for-word
Status: published

I sometimes wonder how often the default paste operation in an
application is appropriate. Maybe I'm abnormal (maybe?) but it seems
like 73.2% of the time, I want pasted text to match the formatting of
where it is going rather than where it came from. I guess the exception
is when I'm copying and pasting from within the same document. The
result is that I use "Paste Special" a lot.

The trouble with Paste Special is that it (a) doesn't have a keyboard
shortcut and (b) brings up a dialog that has to be dealt with when all I
really want is to paste as "Unformatted Text".

My wife is currently a "Knowledge Bowl" coach, and one of her jobs is to
put together a study guide of science vocabulary. That involves a lot of
copying from various sources and pasting into the study guide (which is
a Word document), and finally drove me to come up with a solution. I
found something similar to the following very short macro at
<http://swest.wordpress.com/2006/01/15/ms-word-paste-plain-text/>:

```
Sub PasteSpecialUnformatted()
Selection.PasteAndFormat (wdFormatPlainText)
End Sub
```

You can add this to Normal.dot by clicking the **Macros** button on Word
2007's **View** tab.

Then I customized Word to bind the macro to Ctrl+Shift+V. In Word 2007,
you do this by clicking the Office Menu, then **Word Options**, select
the **Customize** category, click the **Customize...** button by
**Keyboard shortcuts**, which finally brings up the **Customize
Keyboard** dialog. Pick Macros from the **Categories** list to see the
macro, then you can associate a new shortcut key.
