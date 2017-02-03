Title: Object-Oriented vs. Database-Oriented
Date: 2006-02-15 17:00
Author: Eric
Category: Opinion
Slug: object-oriented-vs-database-oriented
Status: published

Having worked for Folio and NextPage, companies that have specialized in
full-text indexing using custom search engines, I have an admitted
knowledge liability with regard to relational databases. It never really
made sense to have a relational database *and* our own search database
coexisting in an application. But it never occurred to me that such a
knowledge liability could be considered a benefit in terms of thinking
about how applications should be designed.<!--more-->

J. Ambrose Little wrote an [editorial about object-oriented design vs.
data-oriented](http://www.devx.com/codemag/Article/30468) design that
solidified some vague thoughts I've had about how one should go about
building software. It has always seemed strange to me when people start
application design based on what the database tables are going to be,
but I thought that might be just due to my own ignorance.

In his article, Little's main point is that applications are frequently
built by shoehorning the domain into a DataSet instead of building
objects specific to the domain. In other words, many people are still
not doing object-oriented design and programming, and gaining the
benefits of domain-specific abstractions. One reason for this is that
Microsoft tools make DataSets really easy. I've found that, while
sometimes seeming like a second-class citizen, I'm able to use
DataSet-like functionality like data binding in Windows Forms with my
own custom objects with reasonably good results.

I'm sure I still need to become better acquainted with traditional
database development, but hopefully my experience will allow a balanced
view of how to design such systems.
