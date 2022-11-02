

/-
  *** Inductive types ***
  Like we mentioned in Lab1, an inductive type is defined through a list of *constructors*, 
  functions whose return type must be the inductive type being constructed.
  Its terms are constructed by applying constructors, in any order and any number of times.
-/

/-
  We already encountered a number of inductive types: `Nat`, `Option`, `List`.
-/

-- WARNING: Things we place `namespace Hidden` are for exemplification purposes only
--          The types below already exist in the core library
namespace Hidden
  inductive Nat 
  | zero : Nat 
  | succ : Nat → Nat 
  -- The terms of `Nat` are of the form: `zero`, `succ zero`, `succ (succ zero)`, ...

  inductive Option (α : Type)
  | none : Option α 
  | some : α → Option α
  -- The terms of `Option α` are of the form: `none` or `some a` for `a : α`.

  inductive List (α : Type)
  | nil : List α 
  | cons : α → List α → List α 
  -- The terms of `List α` are of the form: `nil`, `cons a nil` for some `a : α`, `cons b (cons a nil)` for some other `b : α`, and so on
end Hidden

/-

-/
#check Nat.add -- by right clicking, you can go to the definition of `Nat.add` and observe that it is defined by recursion on the *second* argument
-- Because of this, the following equality is trivial (i.e. it holds *by definition*)
example (n : Nat) : n + 0 = n := by rfl

-- Whereas, for the other, the trivial proof fails
example (n : Nat) : 0 + n = n := by rfl

-- We need to prove this instead by induction on `n`.
attribute [-simp] Nat.zero_add in -- ignore this line, it is just to make things more difficult for didactical purposes
example (n : Nat) : 0 + n = n := by 
  induction n -- we argue by induction on `n`
  -- we get two cases two prove, as when doing induction "on paper"
  case zero => -- if `n` is `0`, the result is trivial
    rfl 
  case succ m ih => -- if `n` is of the form `m + 1`, and we know the statement is true for `m` (in a hypothesis named `ih`)
    rw [Nat.add_succ] -- we can use a core lemma to modify our equality
    rw [ih] -- and the conclusion follows by substituting with the equality we know from inductive hypothesis


/-
  **Exercise 1**: Mimick the structure of the proof by induction above 
  to show the analogous statement for multiplication.
  The lemma `Nat.add_succ` should be replace `Nat.mul_succ` (you can `#check` it if you want to see what it says).
-/

attribute [-simp] Nat.one_mul in
example (n : Nat) : 1 * n = n := by
  induction n
  case zero => 
    rfl
  case succ m ih =>
    rw [Nat.mul_succ]
    rw [ih]

/-
  There is nothing special about induction on naturals.
  We can do proofs by induction on *any* inductive type, for instance on `List`.
-/

variable {α : Type}

/-
  [] is a notation for `nil` and `x :: xs` is a notation for `cons x xs`.
-/
def nth (l : List α) (n : Nat) : Option α := match l, n with 
| [], _ => none
| a :: _, 0 => some a
| _ :: l, n + 1 => nth l n

/-
  **Exercise 2**: Define the `len` function below which should return the length of a given list
-/
def len (l : List α) : Nat := match l with
| [] => 0
| _ :: l => len l + 1

/-
  **Exercise 3**: Prove, by induction on lists, 
  that your definition computes the same values as `List.length` function from the core library.

-/
example (l : List α) : List.length l = len l := by 
  induction l
  case nil =>
    rfl
  case cons a b ih =>
    rw [List.length_cons]
    rw [ih]
    rw [Nat.succ_eq_add_one]
    rfl


/-
  **Exercise 4:** Recall the type `Vector α n` from last time. 
  Then, we convened that a `Vector α n` should be a `List α` together with a proof of the 
  fact that its length is `n`, bundled together in a `structure`.
  Alternatively, we could have defined them from scratch as an inductive type, with no appeal to lists or to their length.
  Write a definition of `Vector α n` as an inductive type.
-/

inductive Vector (α : Type) (n : Nat)
| nil : Vector α n
| cons : α → Vector α n → Vector α n

/-
  **Exercise 5:** To test your `Vector α n` define some functions or prove some theorems of your choice 
  on terms of type `Vector α n`. For instance, you can redo some of the function from Lab4 using the new definition,
  or you can write a function that converts one encoding of vectors into the other.
-/

def list_to_vec (l : List α) : Vector α n := match l with
  | [] => Vector.nil
  | head :: tail => Vector.cons head (list_to_vec tail)

#check list_to_vec [1, 2, 3]

def vec_to_list (v : Vector α n) : List α := match v with 
  | Vector.nil => []
  | Vector.cons head tail => List.cons head (vec_to_list tail)

#check vec_to_list (Vector.cons '3' Vector.nil)

/-
  Bonus thought question: Lean will reject the following inductive definition for being "non positive".
  Beyond technical details, can you come up with an informal explanation of a contradiction 
  that would follow if Lean allowed `BadType` to be defined?
  (`Empty` is a type with no terms, defined simply as an inductive type without any constructor)
-/
inductive BadType 
| badConstructor : (BadType → Empty) → BadType


