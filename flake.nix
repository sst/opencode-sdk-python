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
