import argparse, json
from rankvision.pipeline import RankVisionPipeline

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--asin", required=True)
    p.add_argument("--goals", nargs="*", default=["Improve rank and units sold"])
    p.add_argument("--feedback", nargs="*", default=[],
                   help="Free-form notes like 'CPC too high', 'stockouts last week'")
    args = p.parse_args()

    pipe = RankVisionPipeline()
    result = pipe.run(
        asin=args.asin,
        business_goals=args.goals,
        feedback_notes=args.feedback,
    )
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
