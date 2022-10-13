import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
// import { useNavigate } from "react-router-dom";
import validator from "validator";
// import "../../styles/modules/hometext.css";

function Signup() {
  const { store, actions } = useContext(Context);
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [surname, setSurname] = useState("");
  const [password, setPassword] = useState("");
  const [lister, setLister ] = useState(false);
  const [phone_number, setPhone_number] = useState("");

  const token = localStorage.getItem("token");


//   const navigate = useNavigate();
  const isLoggedIn = isLoggedIn;

  //redirects to profile page if there's a token
//   if (token && token != "" && token != undefined) navigate("/profile");

  // onclick handler to submit info to backend
  const handleClick = () => {
    actions.createNewUser(email, name, password);
    actions.setEmail();
  };

  //email verification
  const [emailError, setEmailError] = useState("Please enter a valid email!");

const validateEmail = (e) => {
    var email = e.target.value;
    if (validator.isEmail(email)) {
      setEmailError("");
    } else {
      setEmailError("Must be a valid email!");
    }
  };

  return (
    <div className="container">
      <div className="">
        <h1 className="mb-3 text-center">Sign Up</h1>

        <div>
          <label className="form-label">Email address</label>
          <input
            type="email"
            className="form-control"
            placeholder="email"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
            onInput={(e) => validateEmail(e)}
          />
          <div className="text-danger">
            <span className="">{emailError}</span>
          </div>
          <label className="form-label">Name</label>
          <input
            type="text"
            className="form-control"
            placeholder="Name"
            value={name}
            onChange={(event) => setName(event.target.value)}
          />
          <div className="text-danger">
            {name == "" || name.length < 2 ? (
              <span>Name must be at least 2 characters long</span>
            ) : (
              <span></span>
            )}
          </div>
          {/* surname section */}
          <label className="form-label">surname</label>
          <input
            type="text"
            className="form-control"
            placeholder="surname"
            value={surname}
            onChange={(event) => setName(event.target.value)}
          />
           {/* phonenumber section */}
           <label className="form-label">Phone Number</label>
          <input
            type="text"
            className="form-control"
            placeholder="Phone Number"
            value={phone_number}
            onChange={(event) => setName(event.target.value)}
          />
           {/* lister section */}
           <label className="form-label">Are you going to add a listing?</label>
          <input
            type="checkbox"
            className=""
            placeholder="Lister"
            value={lister}
            onChange={(event) => setName(event.target.value)}
          />
          <br/>
          <label className="form-label">Password</label>
          <input
            type="password"
            className="form-control"
            placeholder="password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
          />
          <div className="text-danger">
            {password == "" || password.length < 8 ? (
              <span className="p-2">
                Password needs to be at least 8 characters long
              </span>
            ) : (
              <span></span>
            )}
          </div>
        </div>
        <br />
        <div className="text-center">
          <button
            className="btn btn-primary m-1 "
            onClick={handleClick}
            disabled={password.length < 8 || name.length < 2}
          >
            {" "}
            Submit{" "}
          </button>{" "}
        </div>
        <p className="mt-3 text-center">
          {" "}
          Already have an account? <a href="/login"> Login through here </a>
        </p>
      </div>
    </div>
  );
}

export default Signup;