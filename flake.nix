{
  description = "opencode-ai-wg dev toolchain";

  inputs = {
    # nixos-26.05 stable branch, pinned 2026-08-03
    nixpkgs.url = "github:NixOS/nixpkgs/6d65bfc1bcef2ef39a239d38e577e92a89fb0f07";
  };

  outputs =
    { nixpkgs, ... }:
    let
      systems = [
        "x86_64-linux"
        "aarch64-darwin"
      ];
      forAllSystems = nixpkgs.lib.genAttrs systems;
    in
    {
      devShells = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          # Bind mypy to the uv venv interpreter so it resolves the project's
          # dependencies from .venv/lib/python3.*/site-packages. Without this,
          # mypy searches the nix store's site-packages and reports every
          # project import as import-not-found.
          mypy = pkgs.writeShellScriptBin "mypy" ''
            if [ ! -x "$PWD/.venv/bin/python" ]; then
              echo "mypy: no .venv found; run 'nix develop' then 'uv sync' first" >&2
              exit 1
            fi
            exec ${pkgs.mypy}/bin/mypy --python-executable "$PWD/.venv/bin/python" "$@"
          '';
        in
        {
          default = pkgs.mkShell {
            packages = with pkgs; [
              python3
              uv
              ruff
              mypy
              pyright
              # prism mock server runs via npm exec (scripts/mock)
              nodejs_22
            ];
          };
        }
      );
    };
}
