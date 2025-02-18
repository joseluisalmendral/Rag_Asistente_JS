# JSON

**Introducción**

---

JSON (acrónimo de JavaScript Object Notation) es un formato de texto que se utiliza para representar datos estructurados en la forma de objetos. Es muy similar al objeto literal en JavaScript, pero tiene algunas diferencias sintácticas.

Un objeto JSON se representa como una serie de pares clave-valor separados por comas, con las claves entre comillas dobles y los valores pueden ser de cualquier tipo, incluyendo números, cadenas de texto, booleanos o incluso otro objeto o matriz. Las matrices se representan como una lista de valores separados por comas, entre corchetes. Esta sintaxis debe cumplir las siguientes normas:

- Los datos están definidos mediante nombre/valor.
- Los datos están separados por comas.
- Las llaves contienen objetos y los corchetes arrays.

```jsx
"main": "Paul Atreides",

"family":[
  {"firstName":"Leto", "lastName":"Atreides"},
  {"firstName":"Lady", "lastName":"Jessica"},
  {"firstName":"Alia", "lastName":"Atreides"}
]
```

Estos datos son accesibles mediante los métodos tradicionales en JavaScript, permitiendo almacenar todos los datos que queramos, consultarlos, modificarlos o editarlos.

```json
{
  "characters": [
    {
      "id": 1,
      "name": "Luke Skywalker",
      "origin": "Tattooine",
      "role": "Jedi Knight",
      "description": "Luke Skywalker, a Force-sensitive human male, was a legendary Jedi Master who fought in the Galactic Civil War during the reign of the Galactic Empire. Along with his companions, Princess Leia Organa and General Han Solo, Skywalker served as a revolutionary on the side of the Alliance to Restore the Republic—an organization committed to the downfall of the Galactic Empire and the restoration of democracy. Following the war, Skywalker became a living legend, and was remembered as one of the greatest Jedi in galactic history.",
      "image": "image.jpg",
      "portrait": "portrait.jpg"
    },
    {
      "id": 2,
      "name": "Leia Organa",
      "origin": "Alderaan",
      "role": "General",
      "description": "Leia Skywalker Organa Solo was a Force-sensitive human female political and military leader who served in the Alliance to Restore the Republic during the Imperial Era and the New Republic and Resistance in the subsequent New Republic Era. Adopted into the House of Organa, the Alderaanian royal family, she was Princess Leia Organa of Alderaan, a planet in the Core Worlds known for its dedication to pacifism. The princess was raised as the daughter of Senator Bail Prestor Organa and his wife, Queen Breha Organa, making her the heir to the Alderaanian monarchy. Instilled with the values of her adopted homeworld, Organa devoted her life to the restoration of democracy by opposing authoritarian regimes such as the Galactic Empire and the First Order.",
      "image": "image.jpg",
      "portrait": "portrait.jpg"
    },
{...}
	},
"movies": [
    {
      "id": 4,
      "number": "IV",
      "name": "A New Hope",
      "year": 1977,
      "poster": "poster.jpg",
      "trailer": "vZ734NWnAHA",
      "background": "background.jpg",
      "crawl": "It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire. During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet. Pursued by the Empires sinister agents, Princess Leia races home aboard her starship, custodian of the stolen plans that can save her people and restore freedom to the galaxy.",
      "filmMakers": [
        {
          "name": "George Lucas",
          "role": "Director"
        },
        {
          "name": "Gary Kurtz",
          "role": "Producer"
        },
        {
          "name": "Rick McCallum",
          "role": "Producer"
        },
        {
          "name": "John Williams",
          "role": "Score"
        }
      ]
    },
{...}
	]
}
```

**Métodos**

---

**JSON.parse():** Este método nos permite convertir un objeto JSON en un objeto legible por JavaScript que podrá ser usado en la aplicación

```jsx
const char = JSON.parse('{"name":"Steve", "age":140, "city":"New Jersey"}');
```

**JSON.stringify():** Este método convierte un objeto o valor de JavaScript en un string JSON. Esto es bastante útil para almacenar datos, claves o pintar información que de otra manera no se podría, como por ejemplo, almacenar JSON en el localStorage.

```jsx
console.log(JSON.stringify({ "name": "John", "surname": "Snow" }));
//Retorna "{ "name": "John", "surname": "Snow" }"
```