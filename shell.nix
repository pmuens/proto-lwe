with import <nixpkgs> { };

let pythonPackages = python3Packages;

in pkgs.mkShell rec {
  name = "impurePythonEnv";
  venvDir = "./venv";
  buildInputs = [
    pythonPackages.python
    pythonPackages.venvShellHook
  ];

  postVenvCreation = ''
    unset SOURCE_DATE_EPOCH
    pip install -r requirements.txt
  '';

  postShellHook = ''
    # allow pip to install wheels
    unset SOURCE_DATE_EPOCH
  '';
}
