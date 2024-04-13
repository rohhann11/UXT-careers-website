 $ export NIXPKGS_ALLOW_UNSUPPORTED_SYSTEM=1
{
  allowUnsupportedSystem = true;
}
{ pkgs }: {
    deps = [
      pkgs.cowsay
    ];
}