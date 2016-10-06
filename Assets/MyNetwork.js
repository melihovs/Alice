#pragma strict

var WallPrefab : GameObject;

var node_row : int;
var node_col : int;
var dir : String;

function Start () {
    InvokeRepeating( "SendPersonPosition", 2, 0.5 );
}

function Update () {

}

function FixedUpdate () {
    var node_size = WallPrefab.transform.localScale.x;

    node_row = parseInt( transform.position.x / node_size );
    node_col = parseInt( transform.position.z / node_size );

    var x_dir = Camera.main.transform.forward.x;
    var z_dir = Camera.main.transform.forward.z;

    if (
         z_dir > 0 && x_dir < 0 && z_dir > x_dir && Mathf.Abs(z_dir) < Mathf.Abs(x_dir)
          ||
         z_dir < 0 && x_dir < 0 && z_dir > x_dir && Mathf.Abs(z_dir) < Mathf.Abs(x_dir)
    ) {
        dir = 'N';
    }
    else if (
         z_dir < 0 && x_dir > 0 && z_dir < x_dir && Mathf.Abs(z_dir) < Mathf.Abs(x_dir)
          ||
         z_dir > 0 && x_dir > 0 && z_dir < x_dir && Mathf.Abs(z_dir) < Mathf.Abs(x_dir)
    ) {
        dir = 'S';
    }
    else if (
         z_dir > 0 && x_dir < 0 && z_dir > x_dir && Mathf.Abs(z_dir) > Mathf.Abs(x_dir)
          ||
         z_dir > 0 && x_dir > 0 && z_dir > x_dir && Mathf.Abs(z_dir) > Mathf.Abs(x_dir)
    ) {
        dir = 'W';
    }
    else if (
         z_dir < 0 && x_dir < 0 && z_dir < x_dir && Mathf.Abs(z_dir) > Mathf.Abs(x_dir)
          ||
         z_dir < 0 && x_dir > 0 && z_dir < x_dir && Mathf.Abs(z_dir) > Mathf.Abs(x_dir)
    ) {
        dir = 'E';
    }
}

function SendPersonPosition () {
    var form = new WWWForm();
    form.AddField( "node_row", node_row );
    form.AddField( "node_col", node_col );
    form.AddField( "dir", dir );

    var url = "http://vrmaze.it-engine.ru/update_person_position";
    var www = new WWW(url, form);
}
