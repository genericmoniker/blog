Title: .NET BackgroundWorker Summary
Date: 2007-10-10 15:38
Author: Eric
Category: Programming
Tags: .NET
Slug: net-backgroundworker-summary
Status: published

The
[`System.ComponentModel.BackgroundWorker`](http://msdn2.microsoft.com/en-us/library/system.componentmodel.backgroundworker(vs.80).aspx "BackgroundWorker class on MSDN") class
makes it easy to code a long running operation with the ability to
provide progress, cancellation, and notification of completion. It is
particularly nice for UI because while the long running operation
executes on a thread pool thread, notifications of progress and
completion are marshalled back to the "main" thread. (When I say "main"
thread, I mean the one on which `BackgroundWorker.RunWorkerAsync()` is
called.)

<!--more-->These are the steps for using `BackgroundWorker`:

### Setup

1.  **Create an instance of `System.ComponentModel.BackgroundWorker`**.
    This can be done manually, or by adding one as a component with the
    form designer if you're doing UI. Usually you want to store this in
    a member variable so that the instance is available from the
    `DoWork` event handler.
2.  **Add a handler for the `BackgroundWorker.DoWork` event**. This
    handler should implement the long running operation, and will be
    invoked from another thread.
3.  **If you want progress, add a handler for the
    `BackgroundWorker.ProgressChanged` event and set the
    `BackgroundWorker.WorkerReportsProgress` property to true**. This
    event handler will be called on the "main" thread. If you forget to
    enable progress by setting the property, you'll get an
    `InvalidOperationException` if you try to provide progress.
4.  **If you want to allow cancellation, set the
    `BackgroundWorker.WorkerSupportsCancellation` property to true**.
    Likewise, you'll get an `InvalidOperaitonException` if you skip this
    step and try to cancel.
5.  **To get notification of completion, add a handler for the
    `BackgroundWorker.RunWorkerCompleted` event**. This event handler
    will be called on the "main" thread when the long running operation
    stops, either because it is finished or it was cancelled.

### Start

1.  **Start the long running operation by calling
    `BackgroundWorker.RunWorkerAsync`.** You can optionally pass in an
    object that the long running operation can retrieve from the
    `DoWorkEventArgs.Argument` property.

### On the Main Thread

1.  **Call `BackgroundWorker.CancelAsync()` if the long running
    operation ought to be cancelled.** Since the main thread isn't
    blocked, this could be in response to a Cancel button being pressed,
    for example.
2.  **Handle `ProgressChanged` events, if needed.** The
    `ProgressChangedEventArgs.ProgressPercentage` could be used to
    update a progress bar. Additional progress state can be passed from
    the long running operation through the
    `ProgressChangedEventArgs.UserState` property. 
3.  **Handle the `RunWorkerCompleted` event.** There are several
    properties on the `RunWorkerCompletedEventArgs` that can be
    populated from the long running operation. The `Error` property has
    an `Exception` object if one was thrown in the long running
    operation. The `Cancelled` property tells whether the operation was
    cancelled (but see the steps on the worker thread below). The
    `Result` property can be used to retrieve a final outcome of the
    long running operation.

### On the Worker Thread

1.  **Do whatever work is required.** If the operation throws an
    exception, the main thread can retrieve the exception from the
    `RunWorkerCompletedEventArgs.Error` property.
2.  **Check the `BackgroundWorker.CancellationPending` property**. If
    the property is true, cancel the long running operation. Also, when
    the operation is cancelled, you should set `DoWorkEventArgs.Cancel`
    to true so that the `RunWorkerCompletedEventArgs.Cancelled` will
    also be true.
3.  **Call `BackgroundWorker.ReportProgress` as appropriate.** You can
    pass a percent complete and an object with additional progress state
    if desired.
4.  **Set the `DoWorkEventArgs.Result` property when finished.** The
    main thread can retrieve the result, if there is anything
    interesting to pass back to the main thread. 

This post was inspired by Chapter 16 of *Essential C\# 2.0* by Mark
Michaelis.
