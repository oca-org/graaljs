suite = {
  "mxversion" : "6.27.1",

  "name" : "graal-js",

  "version" : "23.1.0",
  "release" : False,
  "groupId" : "org.graalvm.js",
  "url" : "http://www.graalvm.org/",
  "developer" : {
    "name" : "Truffle and Graal developers",
    "email" : "graalvm-users@oss.oracle.com",
    "organization" : "Graal",
    "organizationUrl" : "http://www.graalvm.org/",
  },
  "scm" : {
    "url" : "https://github.com/graalvm/graaljs",
    "read" : "https://github.com/graalvm/graaljs.git",
    "write" : "git@github.com:graalvm/graaljs.git",
  },

  "imports" : {
    "suites" : [
        {
           "name" : "regex",
           "subdir" : True,
           "version" : "f0f46b2161b7d1538f8f5b0f7cd188b5a2cf3f49",
           "urls" : [
                {"url" : "https://github.com/oracle/graal.git", "kind" : "git"},
            ]
        },
    ],
  },

  "repositories" : {
    "graaljs-lafo" : {
      "snapshotsUrl" : "https://curio.ssw.jku.at/nexus/content/repositories/snapshots",
      "releasesUrl": "https://curio.ssw.jku.at/nexus/content/repositories/releases",
      "licenses" : ["UPL", "MIT", "GPLv2-CPE"]
    },
  },

  "licenses" : {
    "UPL" : { #bulk of the code
      "name" : "Universal Permissive License, Version 1.0",
      "url" : "http://opensource.org/licenses/UPL",
    },
  },

  "defaultLicense" : "UPL",

  "javac.lint.overrides" : "none",

  "libraries" : {
    "NETBEANS_PROFILER" : {
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/truffle/js/org-netbeans-lib-profiler-8.2-201609300101.jar"],
      "sha1" : "4b52bd03014f6d080ef0528865c1ee50621e35c6",
    },

    "TESTNASHORN" : {
      "sha1" : "1a31d35e485247e0edf2738a248e1bc2b97f1054",
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/truffle/js/testnashorn-e118c818dbf8.tar.bz2"],
    },

    "TESTNASHORN_EXTERNAL" : {
      "sha1" : "3e3edc251d800bc74f28c78f75844c7086cb5216",
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/truffle/js/testnashorn-external-0f91116bb4bd.tar.bz2"],
    },

    "NASHORN_INTERNAL_TESTS" : {
      "sha1" : "b5840706cc8ce639fcafeab1bc61da2d8aa37afd",
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/truffle/js/nashorn-internal-tests-700f5e3f5ff2.jar"],
    },

    "JACKSON_CORE" : {
      "sha1" : "2ef7b1cc34de149600f5e75bc2d5bf40de894e60",
      "maven" : {
        "groupId" : "com.fasterxml.jackson.core",
        "artifactId" : "jackson-core",
        "version" : "2.8.6",
      },
    },

    "JACKSON_ANNOTATIONS" : {
      "sha1" : "9577018f9ce3636a2e1cb0a0c7fe915e5098ded5",
      "maven" : {
        "groupId" : "com.fasterxml.jackson.core",
        "artifactId" : "jackson-annotations",
        "version" : "2.8.6",
      },
    },

    "JACKSON_DATABIND" : {
      "sha1" : "c43de61f74ecc61322ef8f402837ba65b0aa2bf4",
      "maven" : {
        "groupId" : "com.fasterxml.jackson.core",
        "artifactId" : "jackson-databind",
        "version" : "2.8.6",
      },
    },
  },

  "projects" : {
    "com.oracle.truffle.js" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.js.parser",
        "com.oracle.truffle.js.annotations",
        "com.oracle.truffle.js.codec",
        "com.oracle.truffle.js.runtime.doubleconv",
        "truffle:TRUFFLE_ICU4J",
      ],
      "requires" : [
        "java.management",
        "jdk.management",
        "jdk.unsupported",
      ],
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR", "TRUFFLE_JS_FACTORY_PROCESSOR"],
      "jacoco" : "include",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "checkstyleVersion" : "10.7.0",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.parser" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.js",
      ],
      "jacoco" : "include",
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.js.parser" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "truffle:TRUFFLE_API",
      ],
      "jacoco" : "include",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "checkstyleVersion" : "10.7.0",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.shell" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "sdk:LAUNCHER_COMMON",
        "sdk:JLINE3",
      ],
      "jacoco" : "include",
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.annotations" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [],
      "jacoco" : "include",
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.codec" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "truffle:TRUFFLE_API",
      ],
      "jacoco" : "include",
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.snapshot" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.js.parser",
      ],
      "jacoco" : "include",
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.factory.processor" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.js.annotations",
        "com.oracle.truffle.js.codec",
        "truffle:TRUFFLE_API",
      ],
      "requires": [
        "java.compiler",
      ],
      "jacoco" : "include",
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.runtime.doubleconv" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [],
      "jacoco" : "include",
      "spotbugs" : "false",
#     checkstyle and spotbugs turned off to keep the source aligned
#     with the original nashorn version as much as possible
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.stats" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.js.shell",
        "NETBEANS_PROFILER",
        "com.oracle.truffle.js",
      ],
      "jacoco" : "include",
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.test" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "sdk:GRAAL_SDK",
        "mx:JUNIT",
        "GRAALJS",
        "truffle:TRUFFLE_TCK",
        "com.oracle.truffle.js.snapshot",
      ],
      "requires" : [
        "java.desktop",
        "jdk.unsupported",
      ],
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript",
      "testProject" : True,
    },

    "com.oracle.truffle.js.test.instrumentation" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "mx:JUNIT",
        "com.oracle.truffle.js",
        "com.oracle.truffle.js.parser",
      ],
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript",
      "testProject" : True,
    },

    "com.oracle.truffle.js.test.threading" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "mx:JUNIT",
        "sdk:GRAAL_SDK",
      ],
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript",
      "testProject" : True,
    },

    "com.oracle.truffle.js.test.fetch" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "mx:JUNIT",
        "sdk:GRAAL_SDK",
        "com.oracle.truffle.js.test",
      ],
      "requires" : [
        "java.net.http",
        "jdk.httpserver",
      ],
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript",
      "testProject" : True,
    },

    "com.oracle.truffle.js.scriptengine" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "sdk:GRAAL_SDK",
      ],
      "requires" : [
        "java.scripting",
      ],
      "jacoco" : "include",
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.scriptengine.test" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.js.scriptengine",
        "sdk:GRAAL_SDK",
        "mx:JUNIT",
        "GRAALJS",
      ],
      "requires" : [
        "java.scripting",
        "java.desktop",
      ],
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript",
      "testProject" : True,
    },

    "com.oracle.truffle.js.jmh" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "sdk:GRAAL_SDK",
        "GRAALJS",
        "mx:JMH_1_21"
      ],
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "annotationProcessors" : ["mx:JMH_1_21"],
      "spotbugsIgnoresGenerated" : True,
    },

    "com.oracle.truffle.js.test.external" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "graal-js:GRAALJS",
        "mx:JUNIT",
        "JACKSON_CORE",
        "JACKSON_ANNOTATIONS",
        "JACKSON_DATABIND",
        "NASHORN_INTERNAL_TESTS",
        "TRUFFLE_JS_SNAPSHOT_TOOL",
      ],
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript,Test",
      "testProject" : True,
    },

    "com.oracle.truffle.js.test.sdk" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "mx:JUNIT",
        "sdk:POLYGLOT_TCK"
      ],
      "checkstyle" : "com.oracle.truffle.js",
      "spotbugs" : "true",
      "javaCompliance" : "17+",
      "workingSets" : "Truffle,JavaScript,Test",
      "testProject" : True,
    },

  },

  "distributions" : {
    "GRAALJS" : {
      "moduleInfo" : {
        "name" : "org.graalvm.js",
        "exports" : [
          "com.oracle.truffle.js.lang to org.graalvm.truffle",
          "com.oracle.js.parser.ir to org.graalvm.nodejs",
          "com.oracle.truffle.js.builtins to org.graalvm.nodejs",
          "com.oracle.truffle.js.builtins.helper to org.graalvm.nodejs",
          "com.oracle.truffle.js.lang to org.graalvm.nodejs",
          "com.oracle.truffle.js.nodes to org.graalvm.nodejs",
          "com.oracle.truffle.js.nodes.access to org.graalvm.nodejs",
          "com.oracle.truffle.js.nodes.arguments to org.graalvm.nodejs",
          "com.oracle.truffle.js.nodes.cast to org.graalvm.nodejs",
          "com.oracle.truffle.js.nodes.function to org.graalvm.nodejs",
          "com.oracle.truffle.js.parser to org.graalvm.nodejs",
          "com.oracle.truffle.js.runtime to org.graalvm.nodejs",
          "com.oracle.truffle.js.runtime.array to org.graalvm.nodejs",
          "com.oracle.truffle.js.runtime.builtins to org.graalvm.nodejs",
          "com.oracle.truffle.js.runtime.builtins.wasm to org.graalvm.nodejs",
          "com.oracle.truffle.js.runtime.interop to org.graalvm.nodejs",
          "com.oracle.truffle.js.runtime.objects to org.graalvm.nodejs",
          "com.oracle.truffle.js.runtime.util to org.graalvm.nodejs",
        ],
      },
      "subDir" : "src",
      "dependencies" : [
        "com.oracle.truffle.js",
        "com.oracle.truffle.js.parser",
      ],
      "distDependencies" : [
        "regex:TREGEX",
        "truffle:TRUFFLE_API",
        "sdk:GRAAL_SDK",
        "truffle:TRUFFLE_ICU4J",
      ],
      "exclude" : [
      ],
      "description" : "Graal JavaScript engine",
      "maven" : {
        "artifactId" : "js",
      },
      "license": [
        "UPL",  # Main code
        "MIT",  # JONI regexp engine
      ],
      "allowsJavadocWarnings": True,
    },

    "GRAALJS_LAUNCHER" : {
      "moduleInfo" : {
        "name" : "org.graalvm.js.launcher",
        "exports" : [
            "com.oracle.truffle.js.shell to org.graalvm.launcher",
        ],
      },
      "subDir" : "src",
      "dependencies" : ["com.oracle.truffle.js.shell"],
      "mainClass" : "com.oracle.truffle.js.shell.JSLauncher",
      "distDependencies" : ["sdk:LAUNCHER_COMMON"],
      "exclude" : ["sdk:JLINE3"],
      "description" : "Graal JavaScript Launcher",
      "maven" : {
        "artifactId" : "js-launcher",
      },
      "allowsJavadocWarnings": True,
    },

    "GRAALJS_SCRIPTENGINE" : {
      "moduleInfo" : {
        "name" : "org.graalvm.js.scriptengine",
        "requires" : ["java.scripting"],
        "exports" : [
          "com.oracle.truffle.js.scriptengine",
        ],
      },
      "subDir" : "src",
      "dependencies" : ["com.oracle.truffle.js.scriptengine"],
      "distDependencies" : [
        "sdk:GRAAL_SDK"
      ],
      "description" : "Graal JavaScript ScriptEngine",
      "maven" : {
        "artifactId" : "js-scriptengine",
      },
      "allowsJavadocWarnings": True,
    },

    "TRUFFLE_JS_FACTORY_PROCESSOR" : {
      "subDir" : "src",
      "dependencies" : ["com.oracle.truffle.js.factory.processor"],
      "distDependencies" : [
        "truffle:TRUFFLE_API",
        "sdk:GRAAL_SDK"
      ],
      "maven" : False,
      "overlaps" : ["GRAALJS"],
    },

    "TRUFFLE_JS_SNAPSHOT_TOOL" : {
      "subDir" : "src",
      "dependencies" : ["com.oracle.truffle.js.snapshot"],
      "mainClass" : "com.oracle.truffle.js.snapshot.SnapshotTool",
      "distDependencies" : [
        "GRAALJS",
      ],
      "maven" : False,
    },

    "TRUFFLE_STATS" : {
      "subDir" : "src",
      "mainClass" : "com.oracle.truffle.js.stats.heap.HeapDumpAnalyzer",
      "dependencies" : ["com.oracle.truffle.js.stats"],
      "distDependencies" : [
        "GRAALJS",
        "NETBEANS_PROFILER",
        "GRAALJS_LAUNCHER"
      ],
      "maven" : False,
    },

    "GRAALJS_SCRIPTENGINE_TESTS" : {
      "subDir" : "src",
      "dependencies" : ["com.oracle.truffle.js.scriptengine.test"],
      "distDependencies" : [
        "mx:JUNIT",
        "sdk:GRAAL_SDK",
        "GRAALJS",
        "GRAALJS_SCRIPTENGINE",
      ],
      "maven" : False,
    },

    "TRUFFLE_JS_TESTS" : {
      "dependencies" : [
        "com.oracle.truffle.js.test",
        "com.oracle.truffle.js.test.external",
        "com.oracle.truffle.js.test.fetch",
        "com.oracle.truffle.js.test.instrumentation",
        "com.oracle.truffle.js.test.threading",
      ],
      "exclude" : [
        "mx:HAMCREST",
        "mx:JUNIT",
        "JACKSON_CORE",
        "JACKSON_ANNOTATIONS",
        "JACKSON_DATABIND",
        "NASHORN_INTERNAL_TESTS",
      ],
      "distDependencies" : [
        "GRAALJS",
        "truffle:TRUFFLE_TCK",
        "TRUFFLE_JS_SNAPSHOT_TOOL",
      ],
      "license": [
        "UPL",
      ],
      "maven" : False,
      "description" : "Graal JavaScript Tests",
      "allowsJavadocWarnings": True,
    },

    "SDK_JS_TESTS" : {
      "subDir" : "src",
      "javaCompliance" : "17+",
      "dependencies" : ["com.oracle.truffle.js.test.sdk"],
      "exclude" : [
        "mx:JUNIT",
      ],
      "distDependencies" : [
        "sdk:POLYGLOT_TCK"
      ],
      "maven" : False
    },

    "GRAALJS_GRAALVM_SUPPORT" : {
      "native" : True,
      "description" : "Graal.js support distribution for the GraalVM",
      "layout" : {
        "native-image.properties": "file:mx.graal-js/native-image.properties",
        "./": [
          "file:README.md",
        ],
      },
    },

    "GRAALJS_GRAALVM_LICENSES" : {
      "fileListPurpose": 'native-image-resources',
      "native" : True,
      "description" : "Graal.js license files for the GraalVM",
      "layout" : {
        "LICENSE_GRAALJS.txt" : "file:LICENSE_GRAALJS",
        "THIRD_PARTY_LICENSE_GRAALJS.txt": "file:THIRD_PARTY_LICENSE_GRAALJS.txt",
      },
    },

    "JS_INTEROP_MICRO_BENCHMARKS" : {
      "subDir" : "src",
      "description" : "Graal.js JMH Interop Suite",
      "dependencies" : ["com.oracle.truffle.js.jmh"],
      "exclude" : [
        "mx:JUNIT"
      ],
      "distDependencies" : [
        "sdk:GRAAL_SDK",
        "GRAALJS"
      ],
      "maven" : False,
    }
  }
}
