let travelStackTwo = [
	{
	"start": "Los Angeles",
	"end": "San Francisco"
	},
	{
	"start": "New York",
	"end": "Chicago"
	},
	{
	"start": "San Francisco",
	"end": "Seattle"
	},
	{
	"start": "Chicago",
	"end": "Phoenix"
	},
	{
	"start": "Boston",
	"end": "New York"
	},
	{
	"start": "Phoenix",
	"end": "Los Angeles"
	}
];
let sortedTravelStack = [];
let hashTravelStack = {};
const divFlightElTwo = document.querySelector('#flight-path');
const downArrow = "&darr;";

function createHashStack(travelStack, hashStack) {
	/**
	*Creates a hash table (dictionary) object from an array of travel tickets,
	*utilizing the start and end cities, creating key-value pairs for each ticket.
	*/
	travelStack.forEach((ticket) => {
		let key = ticket.start; //A property that must be named so!
		let value = ticket.end; //A property that must be named so!

		hashStack[key] = value;
	});
	return hashStack;
}

function createKeysArray(hashStack) {
	let keysArr = Object.keys(hashStack);
	return keysArr;
}

function createValuesArray(hashStack) {
	let valuesArr = Object.values(hashStack);
	return valuesArr;
}

function findBeginningCity(keysArray, valuesArray) {
	/**
	*Finds the city (place of origin) in keysArray, as it
	*does not appear in the valuesArray (as a destiniation).
	*/
	for (let i = 0; keysArray[i]; i++) { if (!valuesArray.includes(keysArray[i])) { return keysArray[i]; } }
}

function arrangeTicketOrderDisplayByCity(startPoint, hashStack, htmlElement, travelArrow) {
	/**
	*Sorts the hashStack data by comparing start cities to end cities, after the startPoint.
	*"travelArrow" is a downwards-pointing arrow to signify travel from the location above to the one below.
	*/
	const paraElStart = document.createElement('p');
	paraElStart.setHTML(`<strong>Start: ${startPoint}</strong>`);
	htmlElement.appendChild(paraElStart);
	let nextCity = hashStack[startPoint];

	Object.entries(hashStack).forEach((item) => {
		const paraEl = document.createElement('p');
		paraEl.setHTML(`${travelArrow}<br>${nextCity}`);
		htmlElement.appendChild(paraEl);
		nextCity = hashStack[nextCity];
	});
}

hashTravelStack = createHashStack(travelStackTwo, hashTravelStack);
const travelStackKeys = createKeysArray(hashTravelStack);
const travelStackValues = createValuesArray(hashTravelStack);
const startCity = findBeginningCity(travelStackKeys, travelStackValues);
arrangeTicketOrderDisplayByCity(startCity, hashTravelStack, divFlightElTwo, downArrow);