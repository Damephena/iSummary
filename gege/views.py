from rest_framework import status, viewsets
from rest_framework.response import Response

from common.summarizer import Summarizer

from .models import TextSummary
from .serializers import OriginalTextSerializer, TextSummarySerializer


class SummarizerViewset(viewsets.ModelViewSet):

    """
    create: Create a new text summary based on the original text.
        `Optional`: Include how many sentences you would like the summary to contain.
    list: Get the list of all text summaries in the database.
    partial_update: Update a part of the data such as the summary, original text or title.
    destroy: Delete a summary by ID.
    retrieve: Retrieve a summary by ID
    """

    queryset = TextSummary.objects.all()
    serializer_class = TextSummarySerializer
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "create":
            return OriginalTextSerializer
        return super().get_serializer_class()

    def create(self, request):
        serializer = OriginalTextSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # if no error is raised by our serializer
            # create an instance of the Summarizer tool
            try:
                summary_length = (
                    int(request.data.get("summary_sentence_length")) or None
                )
            except Exception:
                summary_length = None
            summarizer = Summarizer(request.data.get("original_text"), summary_length)
            summary = summarizer.get_summary()
            serializer.save(summarized_text=summary)

            return Response({"detail": "Success", "summary": summary})
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
