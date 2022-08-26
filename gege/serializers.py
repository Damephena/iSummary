from rest_framework import serializers

from .models import TextSummary


class OriginalTextSerializer(serializers.ModelSerializer):
    summary_sentence_length = serializers.IntegerField(
        required=False,
        help_text="How many sentences do you want the original content to be summarized into?",
    )

    class Meta:
        model = TextSummary
        exclude = ["summarized_text"]

    def create(self, validated_data):
        try:
            # if user provides the length they want their summary
            # make sure remove it since the information is not used
            # in TextSummary Model.
            # If we don't remove it, DRF will raise an error that the field does not exist.
            validated_data.pop("summary_sentence_length")
        except Exception:
            # if the field is not there then do nothing.
            ...
        TextSummary.objects.create(**validated_data)
        return validated_data


class TextSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = TextSummary
        fields = "__all__"
