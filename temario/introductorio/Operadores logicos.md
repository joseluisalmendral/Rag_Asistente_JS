# Operadores lógicos

**Introducción**

---

Los operadores lógicos son un tipo de operadores en JavaScript que se utilizan para evaluar expresiones lógicas y devolver un valor booleano (**`true`** o **`false`**). Los operadores lógicos más comunes son **`&&`** (and), **`||`** (or) y **`!`** (not).

**Operador `&&` (and)**

---

El operador **`&&`** evalúa dos expresiones lógicas y devuelve **`true`** si ambas son **`true`**, y **`false`** en cualquier otro caso. La sintaxis del operador **`&&`** es la siguiente:

```jsx
expresión1 && expresión2
```

Aquí tienes algunos ejemplos de cómo funciona el operador **`&&`**:

```jsx
console.log(true && true); // true
console.log(true && false); // false
console.log(false && true); // false
console.log(false && false); // false

```

**Operador `||` (or)**

---

El operador **`||`** evalúa dos expresiones lógicas y devuelve **`true`** si al menos una de ellas es **`true`**, y **`false`** sólo si ambas son **`false`**. La sintaxis del operador **`||`** es la siguiente:

```jsx
expresión1 || expresión2

```

Aquí tienes algunos ejemplos de cómo funciona el operador **`||`**:

```jsx
console.log(true || true); // true
console.log(true || false); // true
console.log(false || true); // true
console.log(false || false); // false

```

**Operador `!` (not)**

---

El operador **`!`** invierte el valor booleano de su operando. Es decir, si el operando es **`true`**, el operador **`!`** lo convierte en **`false`**, y viceversa. La sintaxis del operador **`!`** es la siguiente:

```jsx
!operando

```

Aquí tienes algunos ejemplos de cómo funciona el operador **`!`**:

```jsx
console.log(!true); // false
console.log(!false); // true

```

**Mini-reto**

---

1. Crea una variable llamada **`planet`** y asígnale el valor "Tierra"
2. Crea una variable llamada **`isInnerPlanet`** y asígnale el valor **`true`** (la Tierra es un planeta interno)
3. Crea una variable llamada **`hasAtmosphere`** y asígnale el valor **`true`** (la Tierra tiene atmósfera)
4. Utiliza un operador lógico **`&&`** (AND) para combinar las variables **`isInnerPlanet`** y **`hasAtmosphere`** en una expresión lógica que evalúe a **`true`**. Almacena el resultado en una variable llamada **`isHabitable`**.
5. Utiliza una declaración **`console.log`** para imprimir el valor de la variable **`isHabitable`** en la consola. Debería mostrarse **`true`**.