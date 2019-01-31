from contextlib import contextmanager
from scripting.dynamic import create_dynamic_variable, dynamic_bind, dynamic_append
from scripting.testing import test, skip
from scripting.assertions import assert_equal_results
from scripting.tested import fetch_tested_implementation
from scripting.reference import fetch_reference_implementation
import scripting.reference


@contextmanager
def reference_based_test(identifier):
    ref = fetch_reference_implementation(identifier)
    tested = fetch_tested_implementation(identifier)

    with scripting.reference.reference_based_test(ref, tested) as testcase:
        yield testcase
