import pytest

from logician.configurators.env import EnvListLC
from logician.stdlog.configurator import StdLoggerConfigurator


class TestEnvListLC:
    @pytest.mark.parametrize(
        "env_list",
        [
            ["HOME"],
            ["LOG_LEVEL"],
            ["_DEBUG"],
            ["HOME", "LOG_LEVEL", "_DEBUG"],
        ],
    )
    def test_accepts_valid_env_vars(self, env_list):
        EnvListLC(env_list, StdLoggerConfigurator())

    @pytest.mark.parametrize(
        "env_name",
        [
            "MY-VAR",
            "123ABC",
            "MY VAR",
            "",
            "ENV$VAR",
        ],
    )
    def test_rejects_invalid_env_vars(self, env_name):
        with pytest.raises(ValueError):
            EnvListLC([env_name], StdLoggerConfigurator())

    @pytest.mark.parametrize(
        "env_name",
        [
            "MY-VAR",
            "123ABC",
            "MY VAR",
            "",
            "ENV$VAR",
        ],
    )
    def test_validation_can_be_disabled(self, env_name):
        EnvListLC(
            [env_name],
            StdLoggerConfigurator(),
            validate_env_vars=False,
        )

    def test_clone_preserves_validate_env_vars(self):
        cfg = EnvListLC(
            ["MY-VAR"],
            StdLoggerConfigurator(),
            validate_env_vars=False,
        )
        clone = cfg.clone()
        assert clone._validate_env_vars is False
