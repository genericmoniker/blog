Title: Work Plan Editor - Maintain your personal schedule
Date: 2007-04-23 21:02
Author: Eric
Category: Project
Slug: work-plan-editor
Status: published

**[Install via "ClickOnce"]({static}/downloads/workplan/WorkPlan.application)**  
Version 3.0.2641.36770  
25 Mar 2007  
Around 300 KB

Work Plan Editor depends on the Microsoft .NET Framework 2.0, which can
be obtained through [Windows
Update](http://windowsupdate.microsoft.com "Windows Update").

Note: Installing the software means that you agree to the
[license](/software-license).

Note for **\*\* Firefox \*\*** users: You may need an add-on to use
Microsoft's ClickOnce technology.

[Change History](#change-history)

About Work Plan Editor
----------------------

Work Plan Editor is a tool to help you convert task estimates into a
working schedule that will constantly update itself as you progress
through your tasks. You create a list of tasks, estimate the effort to
complete those tasks (in "ideal" time), add time off that you plan to
take, and Work Plan Editor calculates the actual dates when tasks should
be complete. If you finish a task early, your entire schedule moves up.
If you complete a task late, the schedule is likewise adjusted back. You
can keep a baseline in order to know how your current plan compares to
your original plan.

Work Plan Editor is more focused than an Excel spreadsheet, but simpler than
Microsoft Project. You can read more about the motivation behind it in
[this blog article]({static}/work-plan-editor-release.md).

![Screen Shot]({static}/downloads/workplan/screen-shot.jpg)

### Known Issues

-   Undo/Redo is unreliable. If you do something really bad that needs
    to be undone, consider closing the plan without saving it to revert
    to your previous state.
-   You can't edit your time off entries. The workaround currently is to
    delete and re-add any entries that need to be modified.

If you discover a problem, use the **Help** &gt; **Send Comments or
Report a Bug** menu item to let me know about it.\
[]( "change-history")

### Change History

#### 25 Mar 2007 - Version 3.0.2641.36770

-   Added milestones (see the help file)
-   Added Delete Task menu item

#### 04 Apr 2006 - Version 3.0.2285.35335

-   Fixed the problem where the cells didn't resize correctly according
    to the content when the line wrap option was on
-   Fixed leaking XSLT DLLs
-   Added smart pasting of tab-delimited text

#### 13 Mar 2006 - Version 3.0.2263.38217

-   Finished the Plan Options tab
-   Added auto-complete to the Group/Feature column
-   Added transacted edits - Changes while editing a task can be rolled
    back by hitting Escape
-   Added an Insert After menu item
-   Fixed broken Cut menu
-   Fixed broken Redo menu
-   Several other small user interaction and bug fixes

