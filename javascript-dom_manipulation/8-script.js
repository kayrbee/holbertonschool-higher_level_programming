async function getTranslation () {
  try {
    const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const translation = await response.json();
    const hello = document.getElementById('hello');
    hello.innerHTML = translation.hello;
  } catch (error) {
    console.error(error.message);
  }
}

// Wait for the DOM to finish loading before calling the async function,
// otherwise the <div id='hello'> element is referenced before it exists
document.addEventListener("DOMContentLoaded", (_event) => {
  getTranslation()
})
