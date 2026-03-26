#!/usr/bin/env python3
"""CLI entry point for the Bayesian-Shannon Translation Engine.

Usage:
    python -m scripts.run_pipeline data/raw/transcript.md
    python -m scripts.run_pipeline data/raw/transcript.md --output output/
    python -m scripts.run_pipeline data/raw/transcript.md --config config.yaml
"""

import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.pipeline import (
    TranslationPipeline,
    format_annotated_transcript,
    format_json,
    load_config,
)


def main():
    parser = argparse.ArgumentParser(
        description="Bayesian-Shannon Translation Engine for Chinese-English transcripts"
    )
    parser.add_argument(
        "transcript",
        help="Path to the transcript file (markdown format)",
    )
    parser.add_argument(
        "--config", "-c",
        default="config.yaml",
        help="Path to configuration file (default: config.yaml)",
    )
    parser.add_argument(
        "--output", "-o",
        default="output",
        help="Output directory (default: output/)",
    )
    parser.add_argument(
        "--format", "-f",
        choices=["json", "annotated", "both"],
        default="both",
        help="Output format (default: both)",
    )

    args = parser.parse_args()

    # Read transcript
    transcript_path = Path(args.transcript)
    if not transcript_path.exists():
        print(f"Error: transcript file not found: {transcript_path}")
        sys.exit(1)

    transcript_text = transcript_path.read_text(encoding='utf-8')

    # Load config
    config = load_config(args.config)

    # Run pipeline
    pipeline = TranslationPipeline(config)
    results = pipeline.run(transcript_text)

    # Write output
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.format in ("json", "both"):
        json_path = output_dir / "translation.json"
        json_path.write_text(format_json(results), encoding='utf-8')
        print(f"\nJSON output: {json_path}")

    if args.format in ("annotated", "both"):
        txt_path = output_dir / "translation_annotated.txt"
        txt_path.write_text(
            format_annotated_transcript(results), encoding='utf-8'
        )
        print(f"Annotated output: {txt_path}")

    # Print summary stats
    print(f"\n{'='*40}")
    print(f"Total messages translated: {len(results)}")
    avg_entropy = sum(r.entropy for r in results) / len(results) if results else 0
    print(f"Average entropy: {avg_entropy:.3f}")
    review_count = sum(
        1 for r in results
        if r.confidence_tier.value == 'review'
    )
    print(f"Messages flagged for review: {review_count}")


if __name__ == "__main__":
    main()
