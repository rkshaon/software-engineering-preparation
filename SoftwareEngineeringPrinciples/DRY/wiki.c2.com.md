# Don't Repeat Yourself

## Context
Duplication (inadvertent or purposeful duplication) can lead to maintenance nightmares, poor factoring, and logical contradictions.

Duplication, and the strong possibility of eventual contradiction, can arise anywhere: in architecture, requirements, code, or documentation. The effects can range from mis-implemented code and developer confusion to complete system failure.

One could argue that most of the difficulty in [Y2K remediation](https://en.wikipedia.org/wiki/Year_2000_problem) is due to the lack of a single date abstraction within any given system; the knowledge of dates and date-handling is widely spread.

## The Problem
But what exactly counts as duplication? [CloneAndModifyProgramming](https://wiki.c2.com/?CloneAndModifyProgramming) is generally cited as the chief culprit (see [OnceAndOnlyOnce](https://wiki.c2.com/?OnceAndOnlyOnce), etc.), but there is more to it than that. Whether in code, architecture, requirements documents, or user documentation, duplication of ***knowledge*** - not just text - is the real culprit.

## Therefore
The `DRY (Don't Repeat Yourself)` Principle states:

```
Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.
```

It's okay to have mechanical, textual duplication (the equivalent of caching values: a repeatable, automatic derivation of one source file from some meta-level description), as long as the authoritative source is well known.

For example, in a mixed-language [CORBA environment](https://www.ibm.com/docs/en/integration-bus/9.0.0?topic=corba-common-object-request-broker-architecture) you may choose to treat the [IDL](https://modernidl.idldev.com/) definitions as authoritative. These definitions will be used to automatically generate source code files which duplicate the knowledge in the IDL. But that's okay: the IDL form of the knowledge meets the requirements of our definition.

Where different levels of abstraction are involved, a consistent conflict-resolution scheme must be used. This could be as simple as identifying one level as authoritative in all cases, or always deferring to the high level, or whatever, as long as it is consistently applied.

For example, in `C++` the interface and implementation for a class are typically specified in separate files, duplicating knowledge. You may consider the header file to be authoritative for the contract of the class as viewed by its clients, and the source code to be authoritative regarding issues of implementation which are hidden by the implementation.

*While the duplication between `.c` and `.h` files is annoying, requires extra effort, and discourages the use of private member functions, it doesn't violate DRY because the compiler enforces that the function definition in the `.c` file must match the prototype in the `.h` file.*

**Notes:** This principle is similar to OnceAndOnlyOnce, but with a different objective. With OnceAndOnlyOnce, you are encouraged to refactor to eliminate duplicated code and functionality. With DRY, you try to identify the single, definitive source of every piece of knowledge used in your system, and then use that source to generate applicable instances of that knowledge (code, documentation, tests, etc).

The principle also assumes that your projects have a high degree of automation, allowing the generation of the derivative knowledge artifacts whenever required.

-- [AndrewHunt](https://wiki.c2.com/?AndrewHunt)

### Study Material
- [wiki.c2.com](https://wiki.c2.com/?DontRepeatYourself)