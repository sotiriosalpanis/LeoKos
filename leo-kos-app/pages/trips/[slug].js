

const tripsURL = `${process.env.DETA_ENDPOINT}trips`
const apiKey = process.env.DETA_API_KEY

export async function getStaticProps() {
  const res = await fetch(tripsURL, {
    headers : {
      'X-API-Key': apiKey
    }
  })
  const trips = await res.json()

    return {props: {
      trips,
    }}
  }

export async function getStaticPaths() {
  const res = await fetch(tripsURL, {
    headers : {
      'X-API-Key': apiKey
    }
  })
  const trips = await res.json()
  const paths = trips.map((trip) => ({
    params: { slug: trip._id }
  }))

  return { paths, fallback: false}
}

export default function TripLanding({ trips }) {

  return (
    <h2>Yo</h2>
  )
}