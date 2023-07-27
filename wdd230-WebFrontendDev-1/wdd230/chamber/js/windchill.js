const temperatureF = document.querySelector('#current-temp').textContent;
const windSpeedMPH = document.querySelector('#windSpeedMPH').textContent;
const windChillFactorElem = document.querySelector('#windChillFactor');
/* F = C * 1.8 + 32 */
/* C = (F - 32) / 1.8 */
if (temperatureF <= 50 && windSpeedMPH > 3.0) {
    const windChillFactorF = 35.74 + 0.6215 * temperatureF - 35.75 * windSpeedMPH**(0.16) + 0.4275 * temperatureF * windSpeedMPH**(0.16);
    const windChillFactorC = Math.round((windChillFactorF - 32) / 1.8);
    windChillFactorElem.innerHTML = `${windChillFactorC}&deg;C`;
} else {
    windChillFactorElem.textContent = 'N/A';
}