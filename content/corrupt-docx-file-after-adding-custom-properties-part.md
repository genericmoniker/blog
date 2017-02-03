Title: Corrupt docx File After Adding Custom Properties Part
Date: 2008-03-14 11:15
Author: Eric
Category: How It Works
Tags: Office
Slug: corrupt-docx-file-after-adding-custom-properties-part
Status: published

I spent a few days implementing a component that adds some custom
properties to Office 2007 files. Using the System.IO.Packaging namespace
from .NET 3.0, and looking at some sample code in some [Visual Studio
snippets](http://www.microsoft.com/downloads/details.aspx?FamilyId=8D46C01F-E3F6-4069-869D-90B8B096B556&displaylang=en),
things went pretty smoothly. Just when I thought I was done, though, I
tried opening a manipulated .docx file in Word and got the message "The
file is corrupt and cannot be opened."

<!--more-->

After reproducing the problem a few times, I knew I needed an automated
test for this:

```csharp
[TestMethod]
[Description("Files initially without custom properties can be opened in Word after stamping.")]
[Timeout(20000)]
public void CanOpenStamped()
{
 string testFile = testData.GetFile("NoCustom.docx");
 using (Stream s = new FileStream(testFile, FileMode.Open, FileAccess.ReadWrite))
 {
    IStampable stampable = handler.GetStampable(s);
    stampable.StampNew(Identifier.Generate(), "test server");
 }  

 Word.Application wordApp = null;
 Word.Document wordDoc = null;
try
 {
  wordApp = new Word.Application();
  object fileName = testFile;

  // This will throw if there is an error on open:
  wordDoc = wordApp.Documents.Open(ref fileName, ref missing, ref missing, ref missing,
        ref missing,ref missing, ref missing, ref missing, ref missing, ref missing, ref missing,
        ref missing, ref missing, ref missing, ref missing);
 }
 finally
 {
  if (wordDoc != null)
  {
    Marshal.ReleaseComObject(wordDoc);
  }

  if (wordApp != null)
  {
    ((Word._Application)wordApp).Quit(ref missing, ref missing, ref missing);
    Marshal.ReleaseComObject(wordApp);
  }
 }
}
```

I tried to see if there was any kind of validation tools for OOXML
files, but didn't find anything too helpful. One person said, "If it
opens in Word, it's valid." OK, so what if it isn't valid? How do I
figure it out? There was also a WPML validator, but it was failing on
documents created by Word.

I resorted to creating a bad document (using my code) and making a copy
and opening it in Word 2007. Word offered to fix the document, so I then
had a bad and good version of the document that I could extract and do
diffs on. At first, all I was finding were differences that should be
irrelevant based solely on XML syntax, or minor things that I honestly
didn't know whether they mattered.

Ultimately, I discovered that there was a difference in the
\[ContentTypes\].xml file. The good version had:

```xml
<Override
    PartName="/docProps/custom.xml"
    ContentType="application/vnd.openxmlformats-officedocument.custom-properties+xml"/>
```

The bad version didn't have such an override. This led me to the code
where I created the custom properties part. Changing the specified
content type from "application/xml" to the content type above fixed the
problem. The test passes and hopefully all is now well.
