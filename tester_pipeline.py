import pytest

def test_imports():
    from rankvision.pipeline import RankVisionPipeline
    assert callable(RankVisionPipeline)
