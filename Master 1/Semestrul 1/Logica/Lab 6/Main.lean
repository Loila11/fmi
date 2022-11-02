

/-
  ***IMPLEMENTING LOGICAL SYSTEMS IN LEAN***
-/

/-
  Formula
-/

inductive Formula 
| atomic : Nat → Formula
| negation : Formula → Formula 
| or : Formula → Formula → Formula
| and : Formula → Formula → Formula
| implication : Formula → Formula → Formula 
deriving DecidableEq

namespace Formula

  infixr:50 " ⇒ " => implication
  prefix:80 "∼" => negation
  infixr:30 " ∨ " => or
  infixr:40 " ∧ " => and

  def p₀ := atomic 0
  def p₁ := atomic 1
  def p₂ := atomic 2
  #check p₁ ⇒ p₁

end Formula


/-
  Proof
-/

/-
  Given Γ : List Formula 
        ϕ : Formula 
        Proof Γ ϕ : Type "the type of all proofs of ϕ from Γ"
        Γ ⊢ ϕ   notation Proof Γ φ 
-/


inductive Proof : List Formula → Formula → Type
| ax₁ (Γ : List Formula) (ϕ ψ : Formula) : Proof Γ (ϕ ⇒ (ψ ⇒ ϕ))
| ax₂ (Γ : List Formula) (ϕ ψ χ : Formula) : Proof Γ ((ϕ ⇒ (ψ ⇒ χ)) ⇒ ((ϕ ⇒ ψ) ⇒ (ϕ ⇒ χ)))
| ax₃ (Γ : List Formula) (ϕ ψ : Formula) : Proof Γ ((∼ψ ⇒ ∼ϕ) ⇒ (ϕ ⇒ ψ))
| modusPonens (Γ : List Formula) (ϕ ψ : Formula) : 
  Proof Γ ϕ → Proof Γ (ϕ ⇒ ψ) → Proof Γ ψ
| premise (Γ : List Formula) (γ : Formula) : 
  List.contains Γ γ → Proof Γ γ


/-
  **Exercise 1**: Complete the definition of `Proof` by adding constructors for the rest
  of the propositional axioms (*slide 22 from the course*)
-/ 

/-
  **Exercise 2**: Prove a theorem in the system.
-/
variable (ϕ ψ : Formula)

namespace Proof

  def prf (Γ : List Formula) : Proof Γ _ := 
    ax₁ Γ (∼ψ) (∼ϕ)

  #check prf

  def prf2 (Γ : List Formula) (p : Proof Γ (ϕ ⇒ (ψ ⇒ ϕ))) (q : Proof Γ ((ϕ ⇒ (ψ ⇒ ϕ)) ⇒ (ϕ ⇒ ψ) ⇒ (ϕ ⇒ ϕ))) : Proof Γ _ := 
    (modusPonens Γ (ϕ ⇒ (ψ ⇒ ϕ)) ((ϕ ⇒ ψ) ⇒ (ϕ ⇒ ϕ))) p q

end Proof

