const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			]
		},
		actions: {
			// Use getActions to call a function within a fuction
			createNewUser: async (email, name, password) => {
				const opts = {
				  method: "POST",
				  headers: { "Content-Type": "application/json" },
				  body: JSON.stringify({
					email: email,
					name: name,
					password: password,
				  }),
				};
		
				try {
				  const resp = await fetch(
					process.env.BACKEND_URL + "/api/signup",
		
					opts
				  );
		
				  if (resp.status !== 201) {
					alert("error before initial 201 request");
					return false;
				  }
				  const data = await resp.json();
				  console.log("this came from the backend", data);
				  // need to set up local storage function
				  localStorage.setItem("token", data.access_token);
				  localStorage.setItem("email", email);
		
				  setStore({
					token: data.access_token,
					email: email,
					name: name,
					isLoggedIn: true,
				  });
		
				  return true;
				} catch (error) {
				  console.log("there's an error creating the account");
				  alert("email or username already exists");
				}
			  },
		
			  //setting the token to the localstorage
			  setToken: () => {
				const token = localStorage.getItem("token") || null;
				console.log("this is your token", token);
		
				setStore({ token });
			  },
			  // functionality to log out / remove token
			  logout: () => {
				localStorage.removeItem("token");
				localStorage.removeItem("email");
				console.log("log out triggered");
				setStore({ token: null, team: null, name: null, email: null });
				localStorage.removeItem("team");
			  },
			  // making sure that enail is always set in the store when accessing the dashboard
			  setEmail: () => {
				const email = localStorage.getItem("email");
				 console.log("getemail triggers", email);
				 setStore({ email: email });
			   },
		}
	};
};

export default getState;
