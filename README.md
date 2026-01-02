# Nomad
A safer, smarter and more personal road companion for every traveler.

# Duke AI Hackathon 2025 : Winner Robotics Track 

# Inspiration
Our inspiration came from personal experiences. On one of our trips to Asheville, we missed an important landmark simply because we didn’t know it was there. We realized how easy it is to miss meaningful places after spending hours planning a trip.

We also wanted a way to capture scenic drives without having to hold a phone or mount a camera upfront. That’s when we thought — what if there was a hands-free, voice-controlled travel companion that could both guide and record our journey?

Nomad was born from that idea — a safer, smarter, and more personal road companion for every traveler.

Nomad is a Raspberry Pi-powered car assistant that transforms your windshield into a portal to history. Using computer vision and AI, Nomad automatically captures your surroundings, identifies notable and historic landmarks, and tells you their stories—all through natural conversation.

# What it does
Capture The Raspberry Pi camera continuously monitors the road, intelligently capturing images of road signs, landmarks, and interesting scenery.

Analyze Images are sent to OpenAI's Vision API, which identifies locations, reads signs, and understands the visual context of your surroundings.

Discover AI cross-references your location to discover historical landmarks, finding hidden gems, and notable places nearby.

Engage Nomad conversationally shares discoveries through audio, making every mile more meaningful without distracting from the road.

Remember All captured images are saved and organized into an automatic slideshow, letting you relive your journey anytime.

Nomad is perfect for :

Road Trippers, History Buffs, Families on long drives who love education and entertainment, Educators who can turn field trips into immersive learning experiences, Travel Bloggers and Daily Commuters.

# How we built it

We built Nomad using a Raspberry Pi with a camera module for continuous image capture. The system uses GPT-4o Vision API for real-time landmark detection and GPT-4o-mini for conversational responses. We implemented a semantic memory system using ChromaDB vector database and sentence transformers, allowing Nomad to understand context across your entire journey. Voice interaction is powered by speech recognition with wake word detection, and responses are synthesized using OpenAI's TTS API.

DevPost Link : https://devpost.com/software/nomad-tu59q1

Video Introduction to Nomad : https://ai.invideo.io/workspace/72d502cf-afed-45d6-bc75-95cb6f20b1b6/v40-copilot/1bfe76a3-000e-429f-b97f-054b74027a83
