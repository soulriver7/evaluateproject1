{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.flask
    python3Packages.requests
  ];
  shellHook = ''
    export PYTHONPATH="${pkgs.python3Packages.flask}/lib/python3.10/site-packages:${pkgs.python3Packages.requests}/lib/python3.10/site-packages:$PYTHONPATH"
  '';
}