Title: Mock Object Strategies
Date: 2003-12-09 17:00
Author: Eric
Category: How-To
Slug: mock-object-strategies
Status: published

How do you get your production code to use real objects and your test
code to use mock objects?<!--more-->

Here's the class we want to test (adapted from *Object-Oriented Design
Heuristics*, Arthur J. Riel):

```java
public class HeatFlowRegulator 
{ 
    private Furnace furnace; 
    private Set house;    

    public HeatFlowRegulator(Set house) 
    { 
        this.house = house; 
        furnace = new FurnaceImpl(); 
    }    

    public void poll() 
    { 
        Iterator iter = house.iterator(); 
        while (iter.hasNext()) 
        { 
            Room room = (Room)iter.next(); 
            if (room.isHeatNeeded()) 
            { 
                furnace.on(); 
                return; 
            } 
        }    

        furnace.off(); 
    } 
}
```

Here's the test that we'd like to write:

```java
public void testFurnaceOnIfRoomNeedsHeat() 
{ 
    Set house = new HashSet(); 
    house.add(new Room(€œRoom needing heat€));

    // Hmm€¦ How do I make sure the room needs heat?

    HeatFlowRegulator regulator = new HeatFlowRegulator(house); 
    regulator.poll();    

    // Hmm€¦ How do I know the heat is on or not?
}
```

It looks like we need two mock objects to stand in for `Room` and
`Furnace`. We'll assume here that `Room` and `Furnace` are/can be made
interfaces. When that's not true, things are a little more complicated
(but still possible).

Here's our test after incorporating a mock Room:

```java
public void testFurnaceOnIfRoomNeedsHeat() 
{ 
    Set house = new HashSet(); 
    MockRoom room = new MockRoom(€œRoom needing heat€);
    room.alwaysNeedHeat(); 
    house.add(room);    

    HeatFlowRegulator regulator = new HeatFlowRegulator(house); 
    regulator.poll();    

    // Hmm€¦ How do I know the heat is on or not?
}
```

Let's suppose also that we create a mock `Furnace` that is an `isOn`
method beyond the normal `Furnace` interface. But we're still unable to
finish the test because of this line in the class under test:

```java
 furnace = new FurnaceImpl();
```

Maybe we could have a property that can be set within the test to inform
the HeatFlowRegulator class that it is being tested. The constructor
changes to look something like this:

```java
public HeatFlowRegulator(Set house) 
{ 
    this.house = house; 
    if (testing()) 
        furnace = new MockFurnaceImpl(); 
    else 
        furnace = new FurnaceImpl(); 
}
```

We've successfully substituted the furnace with our mock version, but
we're still no closer to being able to finish the test, because the test
can't get the `MockFurnace` to ask whether it is on or not. Still, just
replacing the real object might be a good first step in the case where a
real `Furnace` implementation is really expensive to work with. This
approach isn't ideal, though, because the behavior of the class being
tested is actually different when in a test situation.

The following sections describe a few approaches for getting our mock
object used that also allow us to finish our test.

### Constructor

If we add a new constructor to HeatFlowRegulator, we can swap in our
mock furnace class:

```java
public HeatFlowRegulator(Set house, Furnace furnace) 
{ 
    this.house = house; 
    this.furnace = furnace; 
}
```

The unit test can then be completed:

```java
public void testFurnaceOnIfRoomNeedsHeat() 
{ 
    Set house = new HashSet(); 
    MockRoom room = new MockRoom(€œRoom needing heat€);
    room.alwaysNeedHeat(); 
    house.add(room);    

    MockFurnace furnace = new MockFurnace(); 
    HeatFlowRegulator regulator = new HeatFlowRegulator(house, furnace); 
    regulator.poll();    

    assertTrue(furnace.isOn()); 
}
```

A nice point about this change to `HeatFlowRegulator` is that existing
clients continue to work exactly as before. A side effect is that the
`Furnace` interface, which was invisible in the public interface before,
is now present. If it really doesn't make sense to expose it, we could
give the new constructor package-level access, and be sure that the test
class is in the same package.

### Setter

If `HeatFlowRegulator` were to have lots of subclasses, it might be
inconvenient to create a new constructor for each subclass. Instead we
might choose to add a setter. The test code would change a little (see
bolded line):

```java
public void testFurnaceOnIfRoomNeedsHeat() 
{ 
    Set house = new HashSet(); 
    MockRoom room = new MockRoom(€œRoom needing heat€);
    room.alwaysNeedHeat(); 
    house.add(room);    

    MockFurnace furnace = new MockFurnace(); 
    HeatFlowRegulator regulator = new HeatFlowRegulator(house); 
    regulator.setFurnace(furnace); 
    regulator.poll();    

    assertTrue(furnace.isOn()); 
}
```

Of course, if the `Furnace` object needed to be used during
construction, this approach wouldn't work so well.

### Factory

What if HeatFlowRegulator worked with multiple furnaces, and it created
them as needed? This changes the example a fair amount, but it's
worthwhile to consider. What we want now is a factory for creating
furnaces, and we want a mock factory to complement the real
implementation. Setting the factory can be done with either of the
previous techniques (constructor or setter). With our mock factory
present, we can return any number of `MockFurnace` implementations.
Here's the new test method:

```java
public void testAnyFurnaceOnIfRoomNeedsHeat() 
{ 
    Set house = new HashSet(); 
    MockRoom room = new MockRoom(€œRoom needing heat€);
    room.alwaysNeedHeat(); 
    house.add(room);    

    MockFurnaceFactory furnaceFactory = new MockFurnaceFactory(); 
    HeatFlowRegulator regulator = new HeatFlowRegulator(house, furnaceFactory); 
    regulator.poll();    

    assertTrue(furnaceFactory.isAnyOn()); 
}
```

We count on our mock factory to hang on to a reference to all the
objects it creates so that we can implement the `isAnyOn` method.

### Static Factory

If you want to hide the factory entirely from the non-test users of your
class -- that is, not change the public interface at all -- you can also
use this approach that [David
Jackman](http://codetest.nextpage.int/weblogs/djackman/articles/173.aspx)
came up with. The basic idea is to have a static factory that can be
replaced at test time with a mock factory instance.

The implementation code calls the factory in a typical singleton
fashion:

```java
Furnace furnace = FurnaceFactory.createFurnace();
```

The factory itself looks like this:

```java
public class FurnaceFactory 
{ 
    protected static FurnaceFactory factoryImpl = new FurnaceFactory();    

    public static Furnace createFurnace() 
    { 
        return factoryImpl.createNewFurnace(); 
    }    

    // singleton, so no access to the constructor
    protected FurnaceFactory() 
    { 
    }    

    protected Furnace createNewFurnace() 
    { 
        return new FurnaceImpl(); 
    } 
}
```

Now you can create a derived mock factory factory to use in testing that
exposes an extra method to override the factory that actually gets used:

```java
public class MockFurnaceFactory extends FurnaceFactory 
{ 
    public static void override() 
    { 
        factoryImpl = new MockFurnaceFactory(); 
    }    

    protected Furnace createNewFurnace() 
    { 
        return new MockFurnaceImpl(); 
    } 
}
```

You would need to call `MockFurnaceFactory.override()` before running
your tests, perhaps in your `setUp` method. There is some danger here,
though, because other tests in the system might need the real factory,
and since it is stored in a static member you need to somehow get it
back to the right instance.

When to use a mock object
-------------------------

From <http://c2.com/cgi/wiki?MockObject>

-   Real object has non-deterministic behavior
-   Real object is difficult to set up
-   Real object has behavior that is hard to cause (such as a
    network error)
-   Real object is slow
-   Real object has (or is) a UI
-   Test needs to query the object, but the queries are not available in
    the real object (for example, "was this callback called?")
-   Real object does not yet exist

Always remember, however, that tests that are decoupled from the class
under test will be more robust than those that have intimate knowledge
of the implementation. Tests are supposed to make it easier to change
the implementation (without fear of breaking everything), not harder.

Resources and References
------------------------

-   [Mock Objects Project](http://mockobjects.com)
-   [Testing in isolation with mock
    objects](http://www.manning.com/massol/massol_chp7.pdf) (PDF) from
    the book *JUnit in Action*.
-   [Using Mock
    Objects](http://www.pragmaticprogrammer.com/starter_kit/ut/mockobjects.pdf) (PDF)
    from the book *Pragmatic Unit Testing in Java with JUnit*
-   [Don't Mock Me: Design Considerations for Mock
    Objects](http://www.agiledevelopmentconference.com/files/XR5-2.pdf) (PDF)

