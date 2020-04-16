{
  "make_global_settings": [
    ["CC", "/usr/bin/clang"],
    ["CXX", "/usr/bin/clang++"]
  ],

  "targets": [
    {
      "target_name": "OSLogger",
      "sources": ["OSLogger.mm", "functions.cc"],
      "include_dirs": ["<!(node -e \"require('nan')\")"],
      "xcode_settings": {
        "CC": "clang",
        "MACOSX_DEPLOYMENT_TARGET": "10.14",
        "CLANG_CXX_LIBRARY": "libc++",
        "OTHER_CPLUSPLUSFLAGS" : ["-std=gnu++14", "-stdlib=libc++"],
        "OTHER_CFLAGS": [
            "-ObjC",
            "-xobjective-c"
        ],
      }
    }
  ]
}
