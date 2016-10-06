#pragma strict
var original_rot;
var original_angle;
var target : GameObject;

function Start () {
	original_rot = Camera.main.transform.rotation;
	original_angle = Camera.main.transform.eulerAngles;
	Debug.Log(Camera.main.transform);
}

function FixedUpdate () {

}

function Update () {
	if (Input.GetButtonDown("Reset")) {
		Camera.main.transform.LookAt(target.transform);
		// transform.rotation = original_rot;
		// Quaternion.Slerp (transform.rotation, original_rot, Time.time * 0.1);
		// Camera.main.transform.rotation = Cardboard.SDK.HeadPose.Orientation;
	}
}
