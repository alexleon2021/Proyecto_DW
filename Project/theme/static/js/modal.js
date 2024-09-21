document.addEventListener('DOMContentLoaded', function() {
    const openModalBtns = document.querySelectorAll('.openModalBtn');
    const closeModalBtn = document.getElementById('closeModalBtn');
    const addModal = document.getElementById('addModal');
    const companyFields = document.getElementById('companyFields');
    let currentField = '';

    // Función para abrir el modal
    function abrirModal(campo) {
        currentField = campo;
        addModal.classList.remove('hidden');
        if (currentField === 'company') {
            companyFields.classList.remove('hidden');
        } else {
            companyFields.classList.add('hidden');
        }
    }

    // Función para cerrar el modal
    function cerrarModal() {
        addModal.classList.add('hidden');
        document.getElementById('newItemInput').value = '';
        document.getElementById('companyImage').value = '';
    }

    // Añadir eventos de clic para abrir el modal
    openModalBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const campo = e.target.dataset.field;
            abrirModal(campo);
        });
    });

    // Añadir evento de clic para cerrar el modal
    closeModalBtn.addEventListener('click', cerrarModal);

    // Manejar el envío del formulario en el modal
    document.getElementById('miFormulario').addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(this);

        fetch('/ruta/a/add_company/', {  // Cambia esto a la URL de tu vista
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')  // Asegúrate de manejar el token CSRF
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.new_field) {
                // Actualizar el formulario principal con el nuevo campo
                document.querySelector('.space-y-4').insertAdjacentHTML('beforeend', data.new_field);
                
                // Ocultar el botón de agregar
                const addButton = document.querySelector(`.openModalBtn[data-field="${currentField}"]`);
                addButton.classList.add('hidden');
            }
            cerrarModal();  // Cierra el modal después de agregar
        })
        .catch(error => console.error('Error:', error));
    });

    // Función para obtener el token CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
