# Discussion Points

1. discount=0 is safe because integers are immutable. cart=[] is dangerous because the same list object is reused.

2. Rebinding assigns a variable to a new object. Mutating changes the existing object.

3. Mutable: list, dict, set
   Immutable: tuple, str, int

4. Yes. Lists are mutable, so changes inside a function are reflected outside when the same list object is passed.
