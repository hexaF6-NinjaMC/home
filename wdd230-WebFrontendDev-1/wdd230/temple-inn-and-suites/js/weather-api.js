const currentDate = new Date();
const currentDayWeek = currentDate.getDay();

// select HTML elements in the document
const alertBox = document.querySelector("#weather-alert");
const weatherCard = document.querySelector("#weather");
const currentTemp = document.querySelector('#current-temp');
const weatherIcon = document.querySelector('#weather-icon');
const captionDesc = document.querySelector('figcaption');

// API key: 4797aacba26ea70a3486fd0a65da0b0e
let lat = 40.5853;
let lon = -105.0844;
let exclusions = ["minutely", "hourly"]
let apiKey = '4797aacba26ea70a3486fd0a65da0b0e';
let units = 'imperial';

const url = `https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${lon}&exclude=${exclusions}&appid=${apiKey}&units=${units}`;

async function apiFetch() {
    try {
        const response = await fetch(url);
        if (response.ok) {
            const data = await response.json();
            displayResults(data);
        } else {
            throw Error(await response.text());
        }
    } catch (error) {
        console.log(error);
    }
}

apiFetch();

function displayResults(weatherData) {
    currentTemp.innerHTML = `<strong>${weatherData.current.temp.toFixed(0)} &deg;F</strong>`;
    const iconSrc = `https://openweathermap.org/img/w/${weatherData.current.weather[0].icon}.png`;
    const desc = weatherData.current.weather[0].description;

    weatherIcon.setAttribute('src', iconSrc);
    weatherIcon.setAttribute('alt', desc);
    captionDesc.textContent = desc;

    if (weatherData.alerts) {
        for (alertItem in weatherData.alerts) {
            alertBox.innerHTML = `Weather Alert: ${weatherData.alerts[alertItem].description} <button class="closeBtn" onclick="closeAlert()">&#10060;</button>`;
        }
    }

    let indeces = 0;
    const forecastHeading = document.createElement('h5');
    forecastHeading.textContent = '3-Day Forecast';
    weatherCard.appendChild(forecastHeading);
    while (indeces < 3) {
        const forecastTemp = document.createElement('h6');
        forecastTemp.innerHTML = `${weatherData.daily[indeces].temp.day.toFixed(0)} &deg;F`;
        weatherCard.appendChild(forecastTemp);
        indeces += 1;
    };
}
    
