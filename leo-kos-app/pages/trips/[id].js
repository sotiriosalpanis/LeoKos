const tripsURL = `${process.env.DETA_ENDPOINT}trips`
const apiKey = process.env.DETA_API_KEY

export async function getStaticProps( {params}) {
  const {id} = params
  const res = await fetch(`${tripsURL}/${id}`, {
    headers : {
      'X-API-Key': apiKey
    }
  })
  const trip = await res.json()
    return {props: {
      trip,
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
    params: { id: trip._id }
  }))

  return { paths, fallback: false}
}

export default function TripLanding({ trip }) {

  return (
    <div>
      <h2>{trip.trip_name}</h2>
      <div>
        {trip.description}
      </div>
      <div>
        {trip.stops.map((stop, index) => {
          return <h3 key={index}>
            {stop.stop_name}
          </h3>
        })}
      </div>
    </div>
  )
}