// today's forecast in Kelvin
const kelvin = 293;

// calculate Celsius
const celsius = kelvin - 273;

// calculate fahrenheit and round down 
let fahrenheit = celsius * (9 / 5) + 32;
fahrenheit = Math.floor(fahrenheit);

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);

// calculate Newton scale and round down
let newton = celsius * (933 / 100);
newton = Math.floor(newton);

console.log(`The temperature is ${newton} degrees Newton`);
