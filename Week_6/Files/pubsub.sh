# Make code_pubsub.py in cloud storage for cloud function

# Copy code_pubsub.py to cloud shell
mkdir pubsub
gsutil cp gs://bdl2022/code_pubsub.py ./pubsub/main.py

# Deploy Cloud Function (Auto creates Topic)
gcloud functions deploy hello_pubsub \
--runtime python39 \
--trigger-topic pubsubtest

# Create Topic (NOT NEEDED)
gcloud pubsub topics create pubsubtest

# Publish
gcloud pubsub topics publish pubsubtest --message SomeRandomName

# Check Logs
gcloud functions logs read --limit 50

# Cleanup
# Delete Cloud Function
gcloud functions delete hello_pubsub