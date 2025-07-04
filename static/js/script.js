function simulateCloud() {
      document.querySelector("header").style.backgroundColor = "#A9BCC8"; // abu mendung
    }
document.getElementById("cityForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const city = document.getElementById("cityInput").value;
    // Simulasi data (bisa diganti dengan API cuaca nantinya)
    const dummyData = {
        city: city,
        temp: 29,
        condition: "Sunny",
        humidity: 60,
        wind: 18
    };

    document.getElementById("cityName").textContent = dummyData.city;
    document.getElementById("temp").textContent = dummyData.temp;
    document.getElementById("condition").textContent = dummyData.condition;
    document.getElementById("humidity").textContent = dummyData.humidity;
    document.getElementById("wind").textContent = dummyData.wind;
    document.getElementById("weather-result").style.display = "block";
});