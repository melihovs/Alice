#pragma strict
var original_pos;

function Start () {
	original_pos = transform.position;
}

function FixedUpdate () {
	if (Input.GetButtonDown("Reset")) {
		transform.position = original_pos;
	}
}

function Update () {

}
