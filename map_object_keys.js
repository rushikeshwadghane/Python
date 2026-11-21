// Demonstrates transforming an object with its keys.

function mapping_data(){
    const m = new Map()
    m.set('id',5)
    console.log('m: ', m);

}


mapping_data()




const person = { name: "Alice", age: 25, city: "Wonderland" };


const transformedObject = Object.fromEntries(
    Object.entries(person).map(([key, value]) => [key.toUpperCase(), value])
);

console.log('person: ', person);
console.log(transformedObject);
// Output: { NAME: 'Alice', AGE: 25, CITY: 'Wonderland' }
