import Iuser from "./userInfo.js";
import Icookies from "../cookie/cookie.js";

export default class editProfileForm extends HTMLElement {
    constructor(){
        super();
        this.attachShadow({mode: 'open'});
	}

	async connectedCallback(){
		const editProfile = document.createElement('div');
		editProfile.id = 'edit-profile';
		this.shadowRoot.appendChild(editProfile);
		await this.initUserInfo();
		this.initFormSubmit();

	}

	async initUserInfo() {
		try {
			const data = await Iuser.getAllUserInfo();
			// Access other properties from data here
			let profilePictureData = data.user.profile_picture_data;
			console.log(data.user.profile_picture);
			this.displayEditProfileForm(data);
		} catch (error) {
			console.error('Error:', error)
		}
	}

	displayEditProfileForm(data){
		let editProfileContainer = this.shadowRoot.querySelector('#edit-profile');
		editProfileContainer.innerHTML = `

		<link rel="stylesheet" href="css/style.css" />
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
		<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"defer></script>
		<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous" defer></script>

		<form id="edit-profile-form" method="post" action="" class="container">
		<div class="mb-4">
			<label for="profile_picture">Profile Picture:</label>
			<input type="file" class="form-control" name="profile_picture" accept="images/*" />
		</div>
		<div class="mb-4">	
			<label for="username">Username:</label>
			<input type="text" class="form-control" id="username" name="username" value="${data.user.username}">
		</div>
		<div class="mb-4">
			<label for="email">Email:</label>
			<input type="email" class="form-control" id="email" name="email" value="${data.user.email}">
		</div>
		<div class="mb-4">
			<label for="first_name">First Name:</label>
			<input type="text" class="form-control" id="first_name" name="first_name" value="${data.user.first_name}">
		</div>
		<div class="mb-4">
			<label for="last_name">Last Name:</label>
			<input type="text" class="form-control" id="last_name" name="last_name" value="${data.user.last_name}">
		</div>
			<button type="submit" class="btn btn-dark">Save changes</button>
		</form>

		`;
	}

	initFormSubmit() {
		const editForm = this.shadowRoot.getElementById('edit-profile-form'); // Use getElementById to find the form within the component
		editForm.addEventListener('submit', function(event) {
			event.preventDefault();
			let jwtToken = Icookies.getCookie('token');
			let csrfToken = Icookies.getCookie('csrftoken');
			const formData = new FormData(editForm);
			fetch('/api/profiles/edit-profile/', {
				method: 'POST',
				body: formData,
				headers: {
					'Authorization': jwtToken,
					'X-CSRFToken': csrfToken
				}
			})
			.then(response => response.json())
			.then(data => {
				if (data.success) {
					console.log('Profile updated successfully');
					// Redirect to the home page
						window.location.href = '/home'; // Change the URL to your home page URL

				} else {
					// Display validation errors or any other error message
					alert('An error occurred. Please try again.');
				}
			})
			.catch(error => {
				console.error('Error:', error);
				// Handle API errors
			});
		});
	}
}

customElements.define('edit-profile-form', editProfileForm);
