document.querySelector('.redirect').addEventListener(
    'click',
    () => {
        document.querySelector('.modal')
            .classList.remove('is-active')
        window.location = 'http://127.0.0.1:8000/landing/home'
    }
)