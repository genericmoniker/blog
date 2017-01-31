Title: Packing and Alignment
Date: 2005-06-24 17:00
Author: Eric
Tags: Windows
Slug: packing-and-alignment
Status: published

I've made some effort to understand the differences between the Struct
Member Alignment compiler option /Zp, `#pragma pack` and
`__declspec(align())` with Microsoft Visual C++ in light of an odd bug
that ultimately was caused by inconsistent packing options between
compilation units.

/Zp and `#pragma pack` are equivalent, but /Zp applies to the whole
compilation unit (if set per source file) or the whole project (if set
as a project option). `#pragma pack` can apply to a subset of a
compilation unit. But they do the same thing: change the alignment of
struct members.

`__declspec(align())`, on the other hand, aligns not the individual data
members of a `struct`, but the `struct` itself. For example:

```cpp
__declspec(align(1)) struct s_align 
{ 
    bool b; 
    int i; 
};
```

The `declspec` above doesn't actually do anything different from what
the default is. If, in contrast, you do this:

```cpp
__declspec(align(32)) struct s_align32 
{ 
    bool b; 
    int i; 
};
```

then `sizeof(s_align32)` is 32, whereas it was 8 in the previous
example. In other words, the `declspec` pads the entire structure to
line up on 32 byte boundaries, but doesn't change the member packing.

In short, if you want binary compatibility with, say, an on-disk
representation of something, you want to pack, not align.
