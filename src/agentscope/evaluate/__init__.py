# -*- coding: utf-8 -*-
"""The evaluation module in AgentScope."""

import importlib

# Lazily import submodule attributes to avoid executing potentially
# side-effectful top-level imports (reduces surprising dependency imports
# and defers warnings such as pkg_resources deprecation until actually used).
_lazy_imports = {
    "EvaluatorBase": ("._evaluator", "EvaluatorBase"),
    "RayEvaluator": ("._evaluator", "RayEvaluator"),
    "GeneralEvaluator": ("._evaluator", "GeneralEvaluator"),

    "MetricBase": ("._metric_base", "MetricBase"),
    "MetricResult": ("._metric_base", "MetricResult"),
    "MetricType": ("._metric_base", "MetricType"),

    "Task": ("._task", "Task"),
    "SolutionOutput": ("._solution", "SolutionOutput"),
    "BenchmarkBase": ("._benchmark_base", "BenchmarkBase"),

    "EvaluatorStorageBase": ("._evaluator_storage", "EvaluatorStorageBase"),
    "FileEvaluatorStorage": ("._evaluator_storage", "FileEvaluatorStorage"),

    "ACEBenchmark": ("._ace_benchmark", "ACEBenchmark"),
    "ACEAccuracy": ("._ace_benchmark", "ACEAccuracy"),
    "ACEProcessAccuracy": ("._ace_benchmark", "ACEProcessAccuracy"),
    "ACEPhone": ("._ace_benchmark", "ACEPhone"),
}


def __getattr__(name):
    """Lazy-load attributes from submodules on first access."""
    if name in _lazy_imports:
        module_name, attr_name = _lazy_imports[name]
        module = importlib.import_module(module_name, __package__)
        value = getattr(module, attr_name)
        globals()[name] = value  # cache for future accesses
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    # Expose the lazily-loadable names in dir() alongside other attributes
    return sorted(list(globals().keys()) + list(_lazy_imports.keys()))


__all__ = [
    "BenchmarkBase",
    "EvaluatorBase",
    "RayEvaluator",
    "GeneralEvaluator",
    "MetricBase",
    "MetricResult",
    "MetricType",
    "EvaluatorStorageBase",
    "FileEvaluatorStorage",
    "Task",
    "SolutionOutput",
    "ACEBenchmark",
    "ACEAccuracy",
    "ACEProcessAccuracy",
    "ACEPhone",
]
